# Generated by Django 4.0.4 on 2022-07-17 11:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0012_multitokens'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='multitokens',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='multitokens',
            name='counterplus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='multitokens',
            unique_together={('user', 'counterplus')},
        ),
    ]
