# Generated by Django 2.1.3 on 2018-12-12 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venter', '0009_auto_20181129_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='email_sent_to',
            field=models.CharField(blank=True, max_length=50, verbose_name='Email Sent to'),
        ),
    ]
