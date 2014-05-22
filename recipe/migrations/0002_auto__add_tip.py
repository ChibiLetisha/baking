# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tip'
        db.create_table(u'recipe_tip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('post', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'recipe', ['Tip'])

        # Adding M2M table for field category on 'Tip'
        m2m_table_name = db.shorten_name(u'recipe_tip_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tip', models.ForeignKey(orm[u'recipe.tip'], null=False)),
            ('category', models.ForeignKey(orm[u'recipe.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tip_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Tip'
        db.delete_table(u'recipe_tip')

        # Removing M2M table for field category on 'Tip'
        db.delete_table(db.shorten_name(u'recipe_tip_category'))


    models = {
        u'recipe.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipe.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['recipe.Category']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipe.tip': {
            'Meta': {'object_name': 'Tip'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['recipe.Category']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['recipe']