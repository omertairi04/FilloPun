# Generated by Django 4.1.3 on 2022-11-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pune', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pune',
            name='image',
            field=models.ImageField(blank=True, default='static/images/default.jpg', null=True, upload_to='profiles/'),
        ),
    ]
