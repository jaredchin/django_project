# Generated by Django 2.0 on 2018-04-09 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_auther'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
    ]
