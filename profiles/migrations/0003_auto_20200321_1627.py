# Generated by Django 3.0.4 on 2020-03-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200318_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='static-user.png', upload_to='photos/%Y/%m/%d/'),
        ),
    ]