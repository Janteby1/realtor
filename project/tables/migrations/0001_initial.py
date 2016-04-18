# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Economic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laborforce', models.DecimalField(decimal_places=5, max_digits=10)),
                ('unemployed', models.DecimalField(decimal_places=5, max_digits=10)),
                ('below_poverty_level', models.DecimalField(decimal_places=5, max_digits=10)),
                ('income_0_50', models.DecimalField(decimal_places=5, max_digits=10)),
                ('income_50_100', models.DecimalField(decimal_places=5, max_digits=10)),
                ('income_100_200', models.DecimalField(decimal_places=5, max_digits=10)),
                ('income_200_plus', models.DecimalField(decimal_places=5, max_digits=10)),
                ('median_income', models.DecimalField(decimal_places=5, max_digits=10)),
                ('mean_income', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='economic',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Neighborhood'),
        ),
    ]
