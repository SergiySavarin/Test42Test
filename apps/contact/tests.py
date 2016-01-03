from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string
from django.test import TestCase

from models import Owner, UsersRequest
from views import contact, requests


class HomePageTest(TestCase):
    """Test contact home page."""
    def test_root_url_resolves_to_home_page_view(self):
        """Test root url and home page url."""
        found = resolve('/')
        self.assertEqual(found.func, contact)

    def test_home_page_returns_correct_html(self):
        """Test site and contact.html content."""
        owner = Owner()
        request = HttpRequest()
        response = render(request, 'contact.html', {'owner': owner})
        expected_html = render_to_string('contact.html')
        self.assertEqual(response.content.decode(), expected_html)


class AdminPageTest(TestCase):
    """Test admin page."""
    def test_admin_page_availiability(self):
        """Test admin page url."""
        response = self.client.get('/admin/')
        self.assertContains(response, 'Django site admin')


class OwnerDataTest(TestCase):
    """Test owner contact model."""
    def test_saving_and_retrieving_owner_data(self):
        """Test saving and retrieving owner data."""
        owner = Owner()

        owner.first_name = 'Sergiy'
        owner.last_name = 'Savarin'
        owner.save()

        saved_data = Owner.objects.all()
        self.assertEqual(saved_data.count(), 2)

        self.assertEqual(saved_data[0].first_name, 'Sergiy')
        self.assertEqual(saved_data[0].last_name, 'Savarin')


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
    def test_saving_request_to_database_after_load_the_page(self):
        """ Test saving request data to database by middleware."""
        start_requests_quantity = UsersRequest.objects.count()
        # Make request to home page
        response = self.client.get('/')
        self.assertContains(response, 'requests')

        end_requests_quantity = UsersRequest.objects.count()
        self.assertEqual(
            start_requests_quantity,
            end_requests_quantity - 1
            )

    def test_storing_requests_to_html_after_new_request(self):
        """ Test saving request data to database by middleware."""
        request = HttpRequest()
        # Add to request META key which make is_ajax() method true
        request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
        response1 = requests(request)
        # Make request to home page
        response2 = self.client.get('/')
        self.assertContains(response2, 'requests')
        # Check request page with new request line
        self.assertContains(response1, 'GET / HTTP/1.1')
