# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(unique=True)),
                ('rate', models.DecimalField(max_digits=8, decimal_places=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
