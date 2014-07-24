# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hours'
        db.create_table(u'enterdata_hours', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['enterdata.Participant'])),
            ('hours_activity', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hours_date', self.gf('django.db.models.fields.DateField')()),
            ('hours_amt', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'enterdata', ['Hours'])


    def backwards(self, orm):
        # Deleting model 'Hours'
        db.delete_table(u'enterdata_hours')


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
            'address_ln1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_ln2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_moveindate': ('django.db.models.fields.DateField', [], {}),
            'address_program': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'address_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"})
        },
        u'enterdata.emergency': {
            'Meta': {'object_name': 'Emergency'},
            'emergency_fname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'emergency_lname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'emergency_phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"})
        },
        u'enterdata.family': {
            'Meta': {'object_name': 'Family'},
            'family_children': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'family_residence': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"})
        },
        u'enterdata.hours': {
            'Meta': {'object_name': 'Hours'},
            'hours_activity': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hours_amt': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hours_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"})
        },
        u'enterdata.khan': {
            'Meta': {'object_name': 'Khan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'khan_dt': ('django.db.models.fields.DateField', [], {}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"})
        },
        u'enterdata.legal': {
            'Meta': {'object_name': 'Legal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_charges': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'legal_convict_dt': ('django.db.models.fields.DateField', [], {}),
            'legal_supervisor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'legal_time_incar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"})
        },
        u'enterdata.literacy_numeracy': {
            'Meta': {'object_name': 'Literacy_numeracy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'litnum_casas': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'litnum_dt': ('django.db.models.fields.DateField', [], {}),
            'litnum_raw': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'litnum_timepoint': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'litnum_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"})
        },
        u'enterdata.orientation': {
            'Meta': {'object_name': 'Orientation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientation_assessdt': ('django.db.models.fields.DateField', [], {}),
            'orientation_compdt': ('django.db.models.fields.DateField', [], {}),
            'orientation_education_level': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'orientation_enrolleddt': ('django.db.models.fields.DateField', [], {}),
            'orientation_firstpayrolldt': ('django.db.models.fields.DateField', [], {}),
            'orientation_group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'orientation_medical_insurance': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'orientation_referral': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'orientation_startdt': ('django.db.models.fields.DateField', [], {}),
            'orientation_supervision': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'orientation_wksp_complete': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'orientation_wksp_enddt': ('django.db.models.fields.DateField', [], {}),
            'orientation_wksp_startdt': ('django.db.models.fields.DateField', [], {}),
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
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'enterdata.probation': {
            'Meta': {'object_name': 'Probation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"}),
            'probation_end_dt': ('django.db.models.fields.DateField', [], {}),
            'probation_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'probation_phone': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'enterdata.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'user_fname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_lname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_login': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'enterdata.voskills': {
            'Meta': {'object_name': 'Voskills'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"}),
            'voskills_ct_driver': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'voskills_osha': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'voskills_osha_card': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'voskills_primary': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'voskills_service': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'enterdata.work_status': {
            'Meta': {'object_name': 'Work_status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enterdata.Participant']"}),
            'wstatus_core_part': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wstatus_exit_dt': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'wstatus_exit_status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wstatus_notes': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wstatus_start_dt': ('django.db.models.fields.DateField', [], {}),
            'wstatus_success': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['enterdata']