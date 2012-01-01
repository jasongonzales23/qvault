# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'FollowUp.person'
        db.delete_column('contactform_followup', 'person_id')

        # Adding field 'FollowUp.contact'
        db.add_column('contactform_followup', 'contact', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['contactform.Contact']), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'FollowUp.person'
        db.add_column('contactform_followup', 'person', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['contactform.Contact']), keep_default=False)

        # Deleting field 'FollowUp.contact'
        db.delete_column('contactform_followup', 'contact_id')


    models = {
        'contactform.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'i_am': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
