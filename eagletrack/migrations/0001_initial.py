# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table('Company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='alpha', max_length=2)),
            ('co', self.gf('django.db.models.fields.related.OneToOneField')(db_index=False, related_name='company_cadet', unique=True, to=orm['eagletrack.Cadet'])),
            ('platoons', self.gf('django.db.models.fields.related.ForeignKey')(related_name='company_platoons', db_index=False, to=orm['eagletrack.Platoon'])),
        ))
        db.send_create_signal(u'eagletrack', ['Company'])

        # Adding model 'Cadet'
        db.create_table('Cadet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('company', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['eagletrack.Company'], unique=True)),
            ('ms_level', self.gf('django.db.models.fields.CharField')(default='one', max_length=4)),
            ('gpa', self.gf('django.db.models.fields.IntegerField')(default=4.0)),
            ('ms_grade', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_company_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'eagletrack', ['Cadet'])

        # Adding model 'Cadre'
        db.create_table('Cadre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('rank', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'eagletrack', ['Cadre'])

        # Adding model 'Platoon'
        db.create_table(u'eagletrack_platoon', (
            (u'company_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['eagletrack.Company'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'eagletrack', ['Platoon'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table('Company')

        # Deleting model 'Cadet'
        db.delete_table('Cadet')

        # Deleting model 'Cadre'
        db.delete_table('Cadre')

        # Deleting model 'Platoon'
        db.delete_table(u'eagletrack_platoon')


    models = {
        u'eagletrack.cadet': {
            'Meta': {'object_name': 'Cadet', 'db_table': "'Cadet'"},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'company': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['eagletrack.Company']", 'unique': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'gpa': ('django.db.models.fields.IntegerField', [], {'default': '4.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_company_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ms_grade': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'ms_level': ('django.db.models.fields.CharField', [], {'default': "'one'", 'max_length': '4'})
        },
        u'eagletrack.cadre': {
            'Meta': {'object_name': 'Cadre', 'db_table': "'Cadre'"},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'eagletrack.company': {
            'Meta': {'object_name': 'Company', 'db_table': "'Company'"},
            'co': ('django.db.models.fields.related.OneToOneField', [], {'db_index': 'False', 'related_name': "'company_cadet'", 'unique': 'True', 'to': u"orm['eagletrack.Cadet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'alpha'", 'max_length': '2'}),
            'platoons': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'company_platoons'", 'db_index': 'False', 'to': u"orm['eagletrack.Platoon']"})
        },
        u'eagletrack.platoon': {
            'Meta': {'object_name': 'Platoon', '_ormbases': [u'eagletrack.Company']},
            u'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['eagletrack.Company']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['eagletrack']