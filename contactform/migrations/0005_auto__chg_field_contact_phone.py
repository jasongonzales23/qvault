# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Contact.phone'
        db.alter_column('contactform_contact', 'phone', self.gf('django.db.models.fields.CharField')(max_length=30))


    def backwards(self, orm):
        
        # Changing field 'Contact.phone'
        db.alter_column('contactform_contact', 'phone', self.gf('django.db.models.fields.CharField')(max_length=11))


    models = {
        'contactform.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'i_am': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'contactform.followup': {
            'Meta': {'object_name': 'FollowUp'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contactform.Contact']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['contactform']
