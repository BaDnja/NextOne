# Generated by Django 3.0.2 on 2020-03-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0006_auto_20200330_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='torrent',
            name='genres',
            field=models.ManyToManyField(to='torrents.Genre'),
        ),
    ]
