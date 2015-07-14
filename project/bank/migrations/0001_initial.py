# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('user', models.ForeignKey(related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
