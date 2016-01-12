from django.core.urlresolvers import reverse
from django.test import TestCase


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
