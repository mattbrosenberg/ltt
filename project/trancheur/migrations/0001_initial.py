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
            name='Bond',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cusip', models.CharField(unique=True, max_length=9)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cusip', models.CharField(max_length=9, unique=True)),
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
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
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('date', models.DateField()),
                ('bond', models.ForeignKey(related_name='prices', to='trancheur.Bond')),
            ],
            options={
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('date', models.DateField()),
                ('bond', models.ForeignKey(to='trancheur.Bond', related_name='prices')),
            ],
            options={
                'get_latest_by': 'date',
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
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
<<<<<<< HEAD
                ('contract_ptr', models.OneToOneField(to='trancheur.Contract', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
=======
                ('contract_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, to='trancheur.Contract', parent_link=True)),
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
                ('coupon', models.DecimalField(decimal_places=5, max_digits=15)),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Residual',
            fields=[
<<<<<<< HEAD
                ('contract_ptr', models.OneToOneField(to='trancheur.Contract', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
=======
                ('contract_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, to='trancheur.Contract', parent_link=True)),
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
                ('payments_per_year', models.IntegerField()),
            ],
            options={
            },
            bases=('trancheur.contract',),
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('time', models.DateTimeField()),
                ('buyer', models.ForeignKey(related_name='purchases', to='users.Investor')),
                ('contract', models.ForeignKey(related_name='trades', to='trancheur.Contract')),
                ('seller', models.ForeignKey(related_name='sales', to='users.Investor')),
            ],
            options={
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('time', models.DateTimeField()),
                ('buyer', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='purchases')),
                ('contract', models.ForeignKey(to='trancheur.Contract', related_name='trades')),
                ('seller', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sales')),
            ],
            options={
                'get_latest_by': 'time',
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contract',
            name='bond',
<<<<<<< HEAD
            field=models.ForeignKey(related_name='contracts', to='trancheur.Bond'),
=======
            field=models.ForeignKey(to='trancheur.Bond', related_name='contracts'),
>>>>>>> a53a21468e83e2268334c725f193a5bb359e9356
            preserve_default=True,
        ),
    ]
