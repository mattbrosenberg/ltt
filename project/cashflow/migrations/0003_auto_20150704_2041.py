# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0002_auto_20150704_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='amount',
            field=models.DecimalField(max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
    ]
