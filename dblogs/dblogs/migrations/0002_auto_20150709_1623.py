# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dblogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('level', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='DBLogEntry',
            new_name='GeneralLog',
        ),
    ]
