# Generated by Django 4.1.3 on 2022-11-21 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_field_alter_profile_profilepic_skills_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='CV',
            field=models.FileField(blank=True, null=True, upload_to='CV/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='Resume/'),
        ),
    ]
