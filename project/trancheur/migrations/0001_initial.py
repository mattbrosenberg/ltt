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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cusip', models.CharField(max_length=9)),
                ('face', models.DecimalField(decimal_places=2, max_digits=15)),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
                ('coupon', models.DecimalField(decimal_places=5, max_digits=15)),
                ('issuance_date', models.DateTimeField()),
                ('maturity', models.DateTimeField()),
                ('payments_per_year', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.DecimalField(decimal_places=2, max_digits=15)),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
                ('issuance_date', models.DateTimeField()),
                ('maturity', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InverseFloater',
            fields=[
                ('contract_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='trancheur.Contract', serialize=False)),
                ('payments_per_year', models.IntegerField()),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='MoneyMarket',
            fields=[
                ('contract_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='trancheur.Contract', serialize=False)),
                ('coupon', models.DecimalField(decimal_places=5, max_digits=15)),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.AddField(
            model_name='contract',
            name='user',
            field=models.ForeignKey(related_name='user', to='users.User'),
            preserve_default=True,
        ),
    ]
