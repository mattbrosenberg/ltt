# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='amount',
            field=models.DecimalField(max_digits=10, decimal_places=5),
            preserve_default=True,
        ),
    ]
