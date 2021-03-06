# Generated by Django 2.2.6 on 2019-10-08 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0006_auto_20191008_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lib_start_page', models.PositiveIntegerField()),
                ('lib_end_page', models.PositiveIntegerField()),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.Scene')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.Show')),
            ],
        ),
    ]
