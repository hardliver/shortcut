# Generated by Django 2.2.12 on 2020-04-07 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortcut', '0004_auto_20200407_0706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='web_path',
            new_name='web_addr',
        ),
    ]
