# Generated by Django 4.0.4 on 2022-04-27 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tittle',
            new_name='title',
        ),
    ]
