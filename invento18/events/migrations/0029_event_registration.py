# Generated by Django 2.0.10 on 2020-02-23 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_auto_20200220_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='registration',
            field=models.TextField(default='yes'),
        ),
    ]
