# Generated by Django 4.2.6 on 2023-12-30 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbase',
            name='country',
        ),
    ]
