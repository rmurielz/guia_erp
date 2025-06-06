# Generated by Django 5.2.1 on 2025-05-19 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdentificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThirdPartyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='terceros_app.country')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200)),
                ('location', models.CharField(choices=[('Nacional', 'Nacional'), ('Exterior', 'Exterior')], max_length=20)),
                ('identification_number', models.CharField(max_length=50, unique=True)),
                ('dv', models.CharField(blank=True, max_length=5, verbose_name='DV')),
                ('address', models.CharField(max_length=200)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='terceros_app.city')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='terceros_app.country')),
                ('identification_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='terceros_app.identificationtype')),
                ('third_party_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='terceros_app.thirdpartytype')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_number', models.IntegerField()),
                ('main_address', models.CharField(max_length=200)),
                ('delivery_address', models.CharField(max_length=200)),
                ('first_name_1', models.CharField(max_length=100)),
                ('first_name_2', models.CharField(blank=True, max_length=100)),
                ('last_name_1', models.CharField(max_length=100)),
                ('last_name_2', models.CharField(blank=True, max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('mobile_phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('third_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='terceros_app.thirdparty')),
            ],
        ),
    ]
