# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Contact.name'
        db.delete_column('contactform_contact', 'name')

        # Adding field 'Contact.first_name'
        db.add_column('contactform_contact', 'first_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=255), keep_default=False)

        # Adding field 'Contact.last_name'
        db.add_column('contactform_contact', 'last_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Contact.name'
        db.add_column('contactform_contact', 'name', self.gf('django.db.models.fields.CharField')(default=0, max_length=255), keep_default=False)

        # Deleting field 'Contact.first_name'
        db.delete_column('contactform_contact', 'first_name')

        # Deleting field 'Contact.last_name'
        db.delete_column('contactform_contact', 'last_name')


    models = {
        'contactform.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'i_am': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'})
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
