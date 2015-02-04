# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserProfile.dog'
        db.delete_column('user_interface_userprofile', 'dog')

        # Deleting field 'UserProfile.balance'
        db.delete_column('user_interface_userprofile', 'balance')

        # Deleting field 'UserProfile.next_appointment'
        db.delete_column('user_interface_userprofile', 'next_appointment')

        # Adding field 'UserProfile.web_url'
        db.add_column('user_interface_userprofile', 'web_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, blank=True, default=''),
                      keep_default=False)

        # Adding field 'UserProfile.support_plan'
        db.add_column('user_interface_userprofile', 'support_plan',
                      self.gf('django.db.models.fields.CharField')(max_length=7, default='None'),
                      keep_default=False)

        # Adding field 'UserProfile.current_balance'
        db.add_column('user_interface_userprofile', 'current_balance',
                      self.gf('django.db.models.fields.DecimalField')(blank=True, max_digits=6, decimal_places=2, default=0.0),
                      keep_default=False)

        # Adding field 'UserProfile.balance_due_date'
        db.add_column('user_interface_userprofile', 'balance_due_date',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True, default=datetime.datetime(2015, 2, 3, 0, 0)),
                      keep_default=False)


        # Changing field 'UserProfile.image'
        db.alter_column('user_interface_userprofile', 'image', self.gf('utilities.ContentTypeRestrictedImageField')(max_length=255, null=True, max_upload_size=2621440))

    def backwards(self, orm):
        # Adding field 'UserProfile.dog'
        db.add_column('user_interface_userprofile', 'dog',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserProfile.balance'
        db.add_column('user_interface_userprofile', 'balance',
                      self.gf('django.db.models.fields.DecimalField')(blank=True, max_digits=6, decimal_places=2, default=0.0),
                      keep_default=False)

        # Adding field 'UserProfile.next_appointment'
        db.add_column('user_interface_userprofile', 'next_appointment',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True, default=datetime.datetime(2015, 2, 3, 0, 0)),
                      keep_default=False)

        # Deleting field 'UserProfile.web_url'
        db.delete_column('user_interface_userprofile', 'web_url')

        # Deleting field 'UserProfile.support_plan'
        db.delete_column('user_interface_userprofile', 'support_plan')

        # Deleting field 'UserProfile.current_balance'
        db.delete_column('user_interface_userprofile', 'current_balance')

        # Deleting field 'UserProfile.balance_due_date'
        db.delete_column('user_interface_userprofile', 'balance_due_date')


        # Changing field 'UserProfile.image'
        db.alter_column('user_interface_userprofile', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=255, null=True))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'user_interface.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'access_token': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True', 'default': "''"}),
            'balance_due_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'blog_url': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'default': "''"}),
            'current_balance': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '6', 'decimal_places': '2', 'default': '0.0'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '40', 'blank': 'True', 'default': "''"}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'blank': 'True', 'unique': 'True', 'null': 'True'}),
            'facebook_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'facebook_open_graph': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'facebook_profile_url': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "''"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('utilities.ContentTypeRestrictedImageField', [], {'max_length': '255', 'blank': 'True', 'null': 'True', 'max_upload_size': '2621440'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "''"}),
            'new_token_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True', 'default': "''"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True', 'default': "''"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'raw_data': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'support_plan': ('django.db.models.fields.CharField', [], {'max_length': '7', 'default': "'None'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'web_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'default': "''"}),
            'website_url': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'default': '85111'})
        }
    }

    complete_apps = ['user_interface']