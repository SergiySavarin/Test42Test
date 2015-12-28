from __future__ import unicode_literals

from django.db import models


class Owner(models.Model):
    """Owner model."""
    first_name = models.CharField(max_length=256, blank=False)
    last_name = models.CharField(max_length=256, blank=False)
    birthday = models.CharField(max_length=256, blank=False)
    email = models.CharField(max_length=256, blank=False)
    skype = models.CharField(max_length=256, blank=False)
    jabber = models.CharField(max_length=256, blank=False)
    # Other information about owner
    other = models.TextField(blank=True)
    # Owner biography
    bio = models.TextField(blank=True)
