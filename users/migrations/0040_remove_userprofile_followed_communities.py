# Generated by Django 3.2.10 on 2022-08-14 14:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0039_userprofile_followed_communities"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="followed_communities",
        ),
    ]
