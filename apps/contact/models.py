from __future__ import unicode_literals

from django.db import models


class Owner(models.Model):
    name = models.TextField(default='')
    last_name = models.TextField(default='')
