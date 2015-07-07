# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trancheur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cashflow',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date', models.DateField()),
                ('contract', models.ForeignKey(related_name='cashflows', to='trancheur.Contract')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=5, max_digits=6)),
                ('date', models.DateField()),
                ('contract', models.ForeignKey(to='trancheur.Contract', related_name='cashflows')),
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
