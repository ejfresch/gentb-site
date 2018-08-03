# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-27 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('mutations', '0009_auto_20171222_1043'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='drug',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='drugclass',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='genome',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='genome',
            name='length',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='strainsource',
            name='resistance_group',
            field=models.CharField(blank=True, choices=[(None, b'Unknown'), (b'S', b'Sensitive'), (b'ODR', b'Other Drug Resistant'), (b'MDR', b'Multi Drug Resistant'), (b'XDR', b'Extensively Drug Resistant')], max_length=4, null=True),
        ),
    ]