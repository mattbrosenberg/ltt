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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date', models.DateField()),
                ('type_of', models.CharField(max_length=20)),
                ('bond', models.ForeignKey(related_name='cashflows', to='trancheur.Bond')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
