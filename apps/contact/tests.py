from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from views import contact

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, contact)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = contact(request)
        expected_html = render_to_string('contact.html')
        self.assertEqual(response.content.decode(), expected_html)
