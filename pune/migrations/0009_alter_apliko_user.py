# Generated by Django 4.1.3 on 2022-11-25 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_delete_businessprofile'),
        ('pune', '0008_remove_pune_aplicants_pune_aplicants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apliko',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to='users.profile'),
        ),
    ]
