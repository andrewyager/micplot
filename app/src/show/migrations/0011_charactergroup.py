# Generated by Django 2.2.6 on 2019-10-08 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0010_auto_20191008_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('characters', models.ManyToManyField(blank=True, to='show.Character')),
                ('scenes', models.ManyToManyField(blank=True, to='show.Scene')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.Show')),
            ],
        ),
    ]
