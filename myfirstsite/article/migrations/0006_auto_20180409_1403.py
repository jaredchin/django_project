# Generated by Django 2.0 on 2018-04-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20180409_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]
