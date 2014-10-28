# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CasTicket'
        db.create_table(u'authentic2_idp_cas_casticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('renew', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('validity', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('expire', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('session_key', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=64, blank=True)),
        ))
        db.send_create_signal(u'authentic2_idp_cas', ['CasTicket'])

        # Adding model 'CasService'
        db.create_table(u'authentic2_idp_cas_casservice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('logout_url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('logout_use_iframe', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('logout_use_iframe_timeout', self.gf('django.db.models.fields.PositiveIntegerField')(default=300)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=128)),
            ('domain', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal(u'authentic2_idp_cas', ['CasService'])


    def backwards(self, orm):
        # Deleting model 'CasTicket'
        db.delete_table(u'authentic2_idp_cas_casticket')

        # Deleting model 'CasService'
        db.delete_table(u'authentic2_idp_cas_casservice')


    models = {
        u'authentic2_idp_cas.casservice': {
            'Meta': {'object_name': 'CasService'},
            'domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logout_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'logout_use_iframe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logout_use_iframe_timeout': ('django.db.models.fields.PositiveIntegerField', [], {'default': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'authentic2_idp_cas.casticket': {
            'Meta': {'object_name': 'CasTicket'},
            'creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expire': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'renew': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'session_key': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '64', 'blank': 'True'}),
            'ticket_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'validity': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['authentic2_idp_cas']