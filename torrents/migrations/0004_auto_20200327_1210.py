# Generated by Django 3.0.4 on 2020-03-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0003_auto_20200327_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrent',
            name='for_parents',
            field=models.BooleanField(default=False),
        ),
    ]