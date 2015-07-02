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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=5, max_digits=6)),
                ('date', models.DateField()),
                ('contract', models.ForeignKey(related_name='cashflows', to='trancheur.Contract')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
