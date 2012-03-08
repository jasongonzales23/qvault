# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Client'
        db.delete_table('contactform_client')

        # Deleting model 'InProcess'
        db.delete_table('contactform_inprocess')

        # Deleting model 'Active'
        db.delete_table('contactform_active')

        # Deleting model 'Inactive'
        db.delete_table('contactform_inactive')

        # Adding field 'Contact.status'
        db.add_column('contactform_contact', 'status', self.gf('django.db.models.fields.CharField')(default='active', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Client'
        db.create_table('contactform_client', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactform.Contact'])),
        ))
        db.send_create_signal('contactform', ['Client'])

        # Adding model 'InProcess'
        db.create_table('contactform_inprocess', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactform.Contact'])),
        ))
        db.send_create_signal('contactform', ['InProcess'])

        # Adding model 'Active'
        db.create_table('contactform_active', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactform.Contact'])),
        ))
        db.send_create_signal('contactform', ['Active'])

        # Adding model 'Inactive'
        db.create_table('contactform_inactive', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactform.Contact'])),
        ))
        db.send_create_signal('contactform', ['Inactive'])

        # Deleting field 'Contact.status'
        db.delete_column('contactform_contact', 'status')


    models = {
        'contactform.contact': {
            'Meta': {'object_name': 'Contact'},
            'application_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'i_am': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '255'})
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
