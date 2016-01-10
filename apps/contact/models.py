from __future__ import unicode_literals

from django.db import models


class Owner(models.Model):
    """Owner model."""
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birthday = models.DateField()
    email = models.EmailField(max_length=256)
    skype = models.CharField(max_length=256)
    jabber = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='image', blank=True, null=True)
    # Other information about owner
    other_info = models.TextField(blank=True)
    # Owner biography
    bio = models.TextField(blank=True)


class UsersRequest(models.Model):
    """Model for storing requests."""
    request_str = models.CharField(max_length=256)
