# Generated by Django 2.2.6 on 2019-10-10 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0016_auto_20191010_2016'),
        ('cast', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='characterinshow',
            unique_together={('run', 'character', 'primary_actor')},
        ),
    ]
