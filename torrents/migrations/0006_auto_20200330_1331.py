# Generated by Django 3.0.2 on 2020-03-30 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0005_auto_20200327_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='torrent',
            name='genres',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
