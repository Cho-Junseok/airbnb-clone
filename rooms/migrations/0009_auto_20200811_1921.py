# Generated by Django 2.2.5 on 2020-08-11 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20200811_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='rooms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rooms.Room'),
        ),
    ]