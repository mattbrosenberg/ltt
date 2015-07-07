# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cusip', models.CharField(unique=True, max_length=9)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('date', models.DateField()),
                ('bond', models.ForeignKey(related_name='prices', to='trancheur.Bond')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('contract_ptr', models.OneToOneField(to='trancheur.Contract', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
                ('coupon', models.DecimalField(decimal_places=5, max_digits=15)),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Residual',
            fields=[
                ('contract_ptr', models.OneToOneField(to='trancheur.Contract', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
                ('payments_per_year', models.IntegerField()),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('time', models.DateTimeField()),
                ('buyer', models.ForeignKey(related_name='purchases', to='users.Investor')),
                ('contract', models.ForeignKey(related_name='trades', to='trancheur.Contract')),
                ('seller', models.ForeignKey(related_name='sales', to='users.Investor')),
            ],
            options={
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
