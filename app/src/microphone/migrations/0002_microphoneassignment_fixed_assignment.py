# Generated by Django 2.2.6 on 2019-10-12 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microphone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='microphoneassignment',
            name='fixed_assignment',
            field=models.BooleanField(default=True),
        ),
    ]
