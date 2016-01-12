import json

from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.shortcuts import render
from django.test import TestCase
from PIL import Image

from apps.contact.models import Owner, UsersRequest
from apps.contact.views import contact, requests
from fortytwo_test_task.settings import BASE_DIR
from apps.contact.resizeimg import resize, size


class HomePageTest(TestCase):
    """Test contact home page."""
    def test_home_page_returns_correct_html(self):
        """Test site and contact.html content."""
        response = self.client.get(reverse('contact'))
        self.assertContains(response, 'Name:')
        self.assertContains(response, 'Last name:')
        self.assertContains(response, 'Skype:')
        self.assertContains(response, 'Bio:')
        self.assertContains(response, 'Photo:')

    def tets_home_page_show_alert_without_owner_data_and_default_image(self):
        """ Test that page show alert message when db is empty and
            default image."""
        request = HttpRequest()
        response = render(request, 'contact.html', {'owner': None})
        self.assertContains(response, 'Database is empty.')
        # Check default image showing
        self.assertContains(response, 'default_user.png')

    def test_home_page_show_edit_option_after_login(self):
        """ Test home page show edit contact option
            when user is already logged in."""
        response = self.client.get(reverse('contact'))
        self.assertNotContains(response, "Edit Contact")
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('contact'))
        self.assertContains(response, "Edit Contact")

    def test_logout_redirect_to_home_page(self):
        """Test that logout redirect to home page."""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('users:auth_logout'))
        response = self.client.get(reverse('contact'))
        self.assertContains(response, "Login")


class OwnerDataView(TestCase):
    """Test owner data view."""
    def test_storing_owner_data_to_html_page(self):
        """Test storing owner data to html."""
        request = HttpRequest()
        response = contact(request)

        self.assertContains(response, 'Sergiy')
        self.assertContains(response, 'Savarin')


class UserRequestsData(TestCase):
    """Test saving and retrieving users requests."""
    def test_saving_request_to_db_after_load_the_page_and_store_to_page(self):
        """ Test saving request data to db by middleware and storing its
            to requests.html page by the right way."""
        # Make request to home page
        response1 = self.client.get(reverse('contact'))
        self.assertContains(response1, 'requests')
        response2 = self.client.get(reverse('contact'))
        self.assertContains(response2, 'requests')
        # Take last request form db
        requests_db = UsersRequest.objects.order_by('id').reverse()[:2]
        request_1_db, request_2_db = requests_db
        # Add to request META key which make is_ajax() method true
        request = HttpRequest()
        request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
        # Take last two requests from requests page
        requests_pg = json.loads(requests(request).content)['request']
        request_1_pg, request_2_pg = requests_pg
        # Check requests page with new requests
        self.assertEqual(request_1_db.request_str, request_1_pg)
        self.assertEqual(request_2_db.request_str, request_2_pg)


class OwnerDataEdit(TestCase):
    """Test for owner data editing."""
    def test_edit_page_show_owner_data_in_fields_after_load(self):
        """Test that edit page after loads show owner data in fields."""
        owner = Owner(
            first_name='Vasja',
            last_name='Pupkin',
            birthday='1965-12-02',
            bio='Nurilsk',
            email='rdb@yans.com',
            skype='lock_lom',
            jabber='vasja@nurilsk.com'
        )
        owner.save()
        # Take dict of owner fields
        owner_fields = Owner.objects.values().first()
        response = self.client.get(reverse('edit_contact'))
        self.assertEqual(response.status_code, 302)
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit_contact'))
        # check each field value from db included in response
        for field in owner_fields:
            if field != 'id' and owner_fields[field] != '':
                self.assertContains(response, owner_fields[field])

    def test_edit_page_show_error_message_after_invalid_data_post(self):
        """ Test that edit page after empty or invalid
            data post shows owner data in fields."""
        self.client.login(username='admin', password='admin')
        # empty post
        response = self.client.post(
            reverse('edit_contact'), {'first_name': ''}
        )
        self.assertEqual(
            response.context['form']['first_name'].errors,
            [u'This field is required.']
        )
        # invalid data post
        response = self.client.post(
            reverse('edit_contact'), {'birthday': 'as;dja sdf'}
        )
        self.assertEqual(
            response.context['form']['birthday'].errors,
            [u'Enter a valid date.']
        )


class OwnerPhotoResize(TestCase):
    """Test for owner photo resizing."""
    def test_resizing_owner_photo_and_save_instaed_original_photo(self):
        """ Test resizing and saving photo instaed original
            photo with same name and ration, max size 200x200px.
        """
        path = '%s/%s' % (
            BASE_DIR, 'apps/contact/tests/data/test_img.jpg'
        )
        testpath = '%s/%s' % (
            BASE_DIR, 'apps/contact/tests/data/test_img_200x200.jpg'
        )
        original = Image.open(path)
        # calculate ratio
        ratio = min(200.0 / original.size[0], 200.0 / original.size[1])
        # calculate new image size
        new_size = (original.size[0] * ratio,  original.size[1] * ratio)
        # resize image and save with testpath
        if not size(path):
            resize(path, testpath)
            test_img = Image.open(testpath)
            # compare test image size with our new_size
            self.assertEqual(new_size[0], test_img.size[0])
            self.assertEqual(new_size[1], test_img.size[1])


class LoginPageTest(TestCase):
    """Test for login page."""
    def test_login_page_returns_correct_html(self):
        """Test login page return correct html."""
        response = self.client.get(reverse('users:auth_login'))
        self.assertContains(response, 'Sign in')

    def test_login_page_returns_alert_message(self):
        """ Test login.html return alert message,
            when user is already logged in."""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('users:auth_login'))
        self.assertContains(response, "Your're already logged in.")


class LoginFormTest(TestCase):
    """Test for login form on login page."""
    def test_login_page_returns_errors_message(self):
        """ Test login from return alert message,
            when user not correct credentials."""
        response = self.client.post(
            reverse('users:auth_login'),
            {'username': 'admin22', 'password': '11admin'}
        )
        self.assertContains(response, "Please, correct the following errors.")

    def test_login_page_redirect_to_home_page_after_login(self):
        """Test login page redirections to home page."""
        # first response redirect us to accounts/profile from login page
        response1 = self.client.post(
            reverse('users:auth_login'),
            {'username': 'admin', 'password': 'admin'}
        )
        self.assertRedirects(
            response1, response1['location'],
            status_code=302, target_status_code=301
        )
        # second response redirect us to home page from accounts profile
        response2 = self.client.get(response1['location'])
        self.assertRedirects(
            response2, reverse('contact'),
            status_code=301, target_status_code=200
        )
