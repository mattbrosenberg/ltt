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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cusip', models.CharField(unique=True, max_length=9)),
                ('face', models.DecimalField(max_digits=15, decimal_places=2)),
                ('coupon', models.DecimalField(max_digits=15, decimal_places=5)),
                ('initial_price', models.DecimalField(max_digits=6, decimal_places=5)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('price', models.DecimalField(max_digits=6, decimal_places=5)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('face', models.DecimalField(max_digits=15, decimal_places=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MoneyMarket',
            fields=[
                ('contract_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='trancheur.Contract', serialize=False, primary_key=True)),
                ('coupon', models.DecimalField(max_digits=15, decimal_places=5)),
                ('issuance_date', models.DateField()),
                ('maturity', models.DateField()),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Residual',
            fields=[
                ('contract_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='trancheur.Contract', serialize=False, primary_key=True)),
                ('payments_per_year', models.IntegerField()),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('price', models.DecimalField(max_digits=6, decimal_places=5)),
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
