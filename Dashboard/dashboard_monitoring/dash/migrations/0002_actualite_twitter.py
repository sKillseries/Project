# Generated by Django 3.0.6 on 2020-05-07 00:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actualite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=42)),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
            ],
            options={
                'verbose_name': 'actualite',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auteur', models.CharField(max_length=100)),
                ('contenu', models.TextField(max_length=280)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
            ],
            options={
                'verbose_name': 'twitter',
                'ordering': ['date'],
            },
        ),
    ]
