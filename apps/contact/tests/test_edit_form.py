from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.contact.models import Owner


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
