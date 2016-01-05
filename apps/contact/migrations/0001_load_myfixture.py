# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'contact.owner': {
            'Meta': {'object_name': 'Owner'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'contact.usersrequest': {
            'Meta': {'object_name': 'UsersRequest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_str': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['contact']
    symmetrical = True
