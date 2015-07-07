# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
<<<<<<< HEAD
=======
from django.conf import settings
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('users', '0001_initial'),
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(related_name='accounts', to='users.Investor')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='accounts')),
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
