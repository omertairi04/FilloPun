# Generated by Django 4.1.3 on 2022-11-24 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_businessprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BusinessProfile',
        ),
    ]