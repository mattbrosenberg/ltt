# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('cusip', models.CharField(max_length=9)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('contract_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='trancheur.Contract')),
                ('coupon', models.DecimalField(decimal_places=5, max_digits=15)),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Residual',
            fields=[
                ('contract_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='trancheur.Contract')),
                ('payments_per_year', models.IntegerField()),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
