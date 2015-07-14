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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('date', models.DateField()),
                ('bond', models.ForeignKey(related_name='prices', to='trancheur.Bond')),
            ],
            options={
                'get_latest_by': 'date',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('face', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type_of', models.CharField(max_length=20)),
                ('is_sold', models.BooleanField(default=False)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MoneyMarket',
            fields=[
                ('contract_ptr', models.OneToOneField(serialize=False, parent_link=True, to='trancheur.Contract', primary_key=True, auto_created=True)),
                ('coupon', models.DecimalField(decimal_places=5, max_digits=15)),
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
                ('contract_ptr', models.OneToOneField(serialize=False, parent_link=True, to='trancheur.Contract', primary_key=True, auto_created=True)),
                ('payments_per_year', models.IntegerField()),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('time', models.DateTimeField()),
                ('buyer', models.ForeignKey(related_name='purchases', to=settings.AUTH_USER_MODEL)),
                ('contract', models.ForeignKey(related_name='trades', to='trancheur.Contract')),
                ('seller', models.ForeignKey(related_name='sales', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'time',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contract',
            name='bond',
            field=models.ForeignKey(related_name='contracts', to='trancheur.Bond'),
            preserve_default=True,
        ),
    ]
