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
            name='Bond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cusip', models.CharField(max_length=9, unique=True)),
                ('face', models.DecimalField(decimal_places=2, max_digits=15)),
                ('coupon', models.DecimalField(decimal_places=5, max_digits=15)),
                ('initial_price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('dated_date', models.DateField()),
                ('auction_date', models.DateTimeField()),
                ('maturity', models.DateField()),
                ('payments_per_year', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BondPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('date', models.DateField()),
                ('bond', models.ForeignKey(to='trancheur.Bond', related_name='prices')),
            ],
            options={
                'get_latest_by': 'date',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.DecimalField(decimal_places=2, max_digits=15)),
                ('issuance_date', models.DateField()),
                ('maturity', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MoneyMarket',
            fields=[
                ('contract_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, to='trancheur.Contract', parent_link=True)),
                ('coupon', models.DecimalField(decimal_places=5, max_digits=15)),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Residual',
            fields=[
                ('contract_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, to='trancheur.Contract', parent_link=True)),
                ('payments_per_year', models.IntegerField()),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('time', models.DateTimeField()),
                ('buyer', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='purchases')),
                ('contract', models.ForeignKey(to='trancheur.Contract', related_name='trades')),
                ('seller', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sales')),
            ],
            options={
                'get_latest_by': 'time',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contract',
            name='bond',
            field=models.ForeignKey(to='trancheur.Bond', related_name='contracts'),
            preserve_default=True,
        ),
    ]
