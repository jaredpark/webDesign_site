# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserProfile.user_profile_placeholder'
        db.delete_column('user_interface_userprofile', 'user_profile_placeholder_id')

        # Adding field 'UserProfile.about_me'
        db.add_column('user_interface_userprofile', 'about_me',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.facebook_id'
        db.add_column('user_interface_userprofile', 'facebook_id',
                      self.gf('django.db.models.fields.BigIntegerField')(null=True, unique=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.access_token'
        db.add_column('user_interface_userprofile', 'access_token',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.facebook_name'
        db.add_column('user_interface_userprofile', 'facebook_name',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.facebook_profile_url'
        db.add_column('user_interface_userprofile', 'facebook_profile_url',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.website_url'
        db.add_column('user_interface_userprofile', 'website_url',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.blog_url'
        db.add_column('user_interface_userprofile', 'blog_url',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.date_of_birth'
        db.add_column('user_interface_userprofile', 'date_of_birth',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.gender'
        db.add_column('user_interface_userprofile', 'gender',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.raw_data'
        db.add_column('user_interface_userprofile', 'raw_data',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.facebook_open_graph'
        db.add_column('user_interface_userprofile', 'facebook_open_graph',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.new_token_required'
        db.add_column('user_interface_userprofile', 'new_token_required',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserProfile.image'
        db.add_column('user_interface_userprofile', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'UserProfile.user_profile_placeholder'
        db.add_column('user_interface_userprofile', 'user_profile_placeholder',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['cms.Placeholder']),
                      keep_default=False)

        # Deleting field 'UserProfile.about_me'
        db.delete_column('user_interface_userprofile', 'about_me')

        # Deleting field 'UserProfile.facebook_id'
        db.delete_column('user_interface_userprofile', 'facebook_id')

        # Deleting field 'UserProfile.access_token'
        db.delete_column('user_interface_userprofile', 'access_token')

        # Deleting field 'UserProfile.facebook_name'
        db.delete_column('user_interface_userprofile', 'facebook_name')

        # Deleting field 'UserProfile.facebook_profile_url'
        db.delete_column('user_interface_userprofile', 'facebook_profile_url')

        # Deleting field 'UserProfile.website_url'
        db.delete_column('user_interface_userprofile', 'website_url')

        # Deleting field 'UserProfile.blog_url'
        db.delete_column('user_interface_userprofile', 'blog_url')

        # Deleting field 'UserProfile.date_of_birth'
        db.delete_column('user_interface_userprofile', 'date_of_birth')

        # Deleting field 'UserProfile.gender'
        db.delete_column('user_interface_userprofile', 'gender')

        # Deleting field 'UserProfile.raw_data'
        db.delete_column('user_interface_userprofile', 'raw_data')

        # Deleting field 'UserProfile.facebook_open_graph'
        db.delete_column('user_interface_userprofile', 'facebook_open_graph')

        # Deleting field 'UserProfile.new_token_required'
        db.delete_column('user_interface_userprofile', 'new_token_required')

        # Deleting field 'UserProfile.image'
        db.delete_column('user_interface_userprofile', 'image')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'user_interface.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about_me': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'access_token': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True', 'default': "''"}),
            'balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2', 'default': '0.0', 'blank': 'True'}),
            'blog_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'default': "''"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dog': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '40', 'blank': 'True', 'default': "''"}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'unique': 'True', 'blank': 'True'}),
            'facebook_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'facebook_open_graph': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_profile_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'new_token_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'next_appointment': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True', 'default': "''"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True', 'default': "''"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'raw_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'website_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'default': '85111', 'max_length': '5'})
        }
    }

    complete_apps = ['user_interface']