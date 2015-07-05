# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trancheur', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='buyer',
            field=models.ForeignKey(related_name='purchases', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trade',
            name='contract',
            field=models.ForeignKey(to='trancheur.Contract'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trade',
            name='seller',
            field=models.ForeignKey(related_name='sales', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contract',
            name='bond',
            field=models.ForeignKey(related_name='contracts', to='trancheur.Bond'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contract',
            name='trades',
            field=models.ManyToManyField(through='trancheur.Trade', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bondprice',
            name='bond',
            field=models.ForeignKey(related_name='prices', to='trancheur.Bond'),
            preserve_default=True,
        ),
    ]
