# Generated by Django 3.0.6 on 2020-05-24 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statergy_name', models.CharField(max_length=255)),
                ('statergy_add_date', models.DateTimeField(default=datetime.datetime)),
                ('statergy_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=50)),
            ],
        ),
    ]
