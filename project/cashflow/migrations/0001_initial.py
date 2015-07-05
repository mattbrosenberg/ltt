# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cashflow',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('amount', models.DecimalField(decimal_places=5, max_digits=6)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
