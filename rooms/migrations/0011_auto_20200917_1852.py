# Generated by Django 2.2.5 on 2020-09-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_auto_20200823_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='How many people'),
        ),
    ]
