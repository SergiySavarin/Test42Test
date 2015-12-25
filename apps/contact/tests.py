from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from models import Owner
from views import contact


class HomePageTest(TestCase):
    """Test contact home page."""
    def test_root_url_resolves_to_home_page_view(self):
        """Test root url and home page url."""
        found = resolve('/')
        self.assertEqual(found.func, contact)

    def test_home_page_returns_correct_html(self):
        """Test site and contact.html content."""
        request = HttpRequest()
        response = contact(request)
        expected_html = render_to_string('contact.html')
        self.assertEqual(response.content.decode(), expected_html)


class OwnerDataTest(TestCase):
    """Test owner contact model."""
    def test_saving_and_retriving_owner_data(self):
        """Test saving and retriving owner data."""
        owner = Owner()

        owner.name = 'Sergiy'
        owner.last_name = 'Savarin'
        owner.save()

        saved_data = Owner.objects.all()
        self.assertEqual(saved_data.count(), 1)

        self.assertEqual(saved_data.name, 'Sergiy')
        self.assertEqual(saved_data.last_name, 'Savarin')
