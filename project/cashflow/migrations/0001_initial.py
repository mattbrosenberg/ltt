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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(max_digits=15, decimal_places=2)),
                ('date', models.DateField()),
                ('contract', models.ForeignKey(related_name='cashflows', to='trancheur.Contract')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
