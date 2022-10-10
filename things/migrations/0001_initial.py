# Generated by Django 4.1.2 on 2022-10-10 14:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Things',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=120)),
                ('quantity', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
