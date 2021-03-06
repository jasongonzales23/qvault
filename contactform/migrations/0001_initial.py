# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Contact'
        db.create_table('contactform_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('i_am', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('contactform', ['Contact'])

        # Adding model 'FollowUp'
        db.create_table('contactform_followup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactform.Contact'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=255)),
        ))
        db.send_create_signal('contactform', ['FollowUp'])


    def backwards(self, orm):
        
        # Deleting model 'Contact'
        db.delete_table('contactform_contact')

        # Deleting model 'FollowUp'
        db.delete_table('contactform_followup')


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
