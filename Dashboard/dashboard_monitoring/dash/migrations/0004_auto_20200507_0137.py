# Generated by Django 3.0.6 on 2020-05-07 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_auto_20200507_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualite',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vulnerabilite',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
