# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trancheur', '0001_initial'),
        ('cashflow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashflow',
            name='contract',
            field=models.ForeignKey(related_name='cashflows', to='trancheur.Contract'),
            preserve_default=True,
        ),
    ]
