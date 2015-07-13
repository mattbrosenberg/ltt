# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashflow',
            name='bond',
        ),
        migrations.RemoveField(
            model_name='cashflow',
            name='date',
        ),
        migrations.RemoveField(
            model_name='cashflow',
            name='type_of',
        ),
    ]
