# Generated by Django 2.2.5 on 2020-08-23 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20200811_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Accuracy',
            new_name='accuracy',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Check_in',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Cleanliness',
            new_name='cleanliness',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Communication',
            new_name='communication',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Value',
            new_name='value',
        ),
        migrations.AlterField(
            model_name='review',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='rooms.Room'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
