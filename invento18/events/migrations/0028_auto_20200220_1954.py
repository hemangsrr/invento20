# Generated by Django 2.0.10 on 2020-02-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0027_event_linkurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.TextField(),
        ),
    ]