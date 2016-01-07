import json

from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.shortcuts import render
from django.test import TestCase

from models import Owner, UsersRequest
from views import contact, requests


class HomePageTest(TestCase):
    """Test contact home page."""
    def test_home_page_returns_correct_html(self):
        """Test site and contact.html content."""
        response = self.client.get(reverse('contact'))
        self.assertContains(response, 'Name:')
        self.assertContains(response, 'Last name:')
        self.assertContains(response, 'Skype:')
        self.assertContains(response, 'Bio:')

    def tets_home_page_show_alert_without_owner_data_and_default_image(self):
        """ Test that page show alert message when db is empty and
            default image."""
        request = HttpRequest()
        response = render(request, 'contact.html', {'owner': None})
        self.assertContains(response, 'Database is empty.')
        # Check default image showing
        self.assertContains(response, 'default_user.png')


class OwnerDataView(TestCase):
    """Test owner data view."""
    def test_storing_owner_data_to_html_page(self):
        """Test storing owner data to html."""
        owner = Owner()

        owner.first_name = 'Sergiy'
        owner.last_name = 'Savarin'
        owner.save()

        request = HttpRequest()
        response = contact(request)

        self.assertContains(response, 'Sergiy')
        self.assertContains(response, 'Savarin')


class UserRequestsData(TestCase):
    """Test saving and retrieving users requests."""
    def test_saving_request_to_db_after_load_the_page_and_store_to_page(self):
        """ Test saving request data to db by middleware and storing its
            to requests.html page by the right way."""
        request = HttpRequest()
        # Make request to home page
        response1 = self.client.get(reverse('contact'))
        self.assertContains(response1, 'requests')
        response2 = self.client.get(reverse('contact'))
        self.assertContains(response2, 'requests')
        # Take last request form db
        requests_db = UsersRequest.objects.order_by('id').reverse()[:2]
        request_1_db, request_2_db = requests_db
        # Add to request META key which make is_ajax() method true
        request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
        # Take last two requests from requests page
        requests_pg = json.loads(requests(request).content)['request']
        request_1_pg, request_2_pg = requests_pg
        # Check requests page with new requests
        self.assertEqual(request_1_db.request_str, request_1_pg[3:-4])
        self.assertEqual(request_2_db.request_str, request_2_pg[3:-4])


class OwnerDataEdit(TestCase):
    """Test for owner data editing."""
    def test_edit_page_show_owner_data_in_fields_after_load(self):
        """Test that edit page after load show owner data in fields."""
        owner = Owner(
            first_name='Vasja',
            last_name='Pupkin',
            bio='Nurilsk',
            email='rdb@yans.com',
            skype='lock_lom',
        )
        owner.save()
        # Take dict of owner fields
        owner_fields = Owner.objects.values().first()
        response = self.client.get(reverse('edit_contact'))
        # check each field value from db included in response
        for field in owner_fields:
            if field not in ['', 'id']:
                self.assertContains(response, owner_fields[field])
