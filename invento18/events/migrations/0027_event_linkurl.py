# Generated by Django 2.0.10 on 2020-02-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_auto_20200218_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='linkurl',
            field=models.URLField(blank=True),
        ),
    ]
