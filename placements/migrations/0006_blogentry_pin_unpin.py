# Generated by Django 3.1.2 on 2021-07-16 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0005_auto_20181001_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='pin_unpin',
            field=models.BooleanField(default=False),
        ),
    ]
