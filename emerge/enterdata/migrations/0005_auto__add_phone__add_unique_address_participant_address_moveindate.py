# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Phone'
        db.create_table(u'enterdata_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['enterdata.Participant'])),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('phone_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'enterdata', ['Phone'])

        # Adding unique constraint on 'Address', fields ['participant', 'address_moveindate']
        db.create_unique(u'enterdata_address', ['participant_id', 'address_moveindate'])


    def backwards(self, orm):
        # Removing unique constraint on 'Address', fields ['participant', 'address_moveindate']
        db.delete_unique(u'enterdata_address', ['participant_id', 'address_moveindate'])

        # Deleting model 'Phone'
        db.delete_table(u'enterdata_phone')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'enterdata.address': {
            'Meta': {'unique_together': "(('participant', 'address_moveindate'),)", 'object_name': 'Address'},
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_ln1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_ln2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_moveindate': ('django.db.models.fields.DateField', [], {}),
            'address_program': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'address_zipcode': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"})
        },
        u'enterdata.participant': {
            'Meta': {'object_name': 'Participant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant_age': ('django.db.models.fields.IntegerField', [], {}),
            'participant_fname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'participant_gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'participant_lname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'participant_prefix': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'participant_race': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'participant_suffix': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'enterdata.phone': {
            'Meta': {'object_name': 'Phone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"}),
            'phone_date': ('django.db.models.fields.DateField', [], {}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'enterdata.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'user_fname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_lname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_login': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['enterdata']