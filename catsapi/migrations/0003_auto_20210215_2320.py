# Generated by Django 3.1.6 on 2021-02-15 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catsapi', '0002_auto_20210215_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='возраст',
            new_name='birth',
        ),
        migrations.RenameField(
            model_name='cat',
            old_name='имя',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='cat',
            old_name='вес',
            new_name='weight',
        ),
    ]
