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
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
                ('date', models.DateField(unique=True)),
                ('rate', models.DecimalField(decimal_places=5, max_digits=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
