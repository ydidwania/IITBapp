# Generated by Django 2.0.5 on 2018-06-18 16:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='MenuEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('day', models.IntegerField()),
                ('breakfast', models.TextField(blank=True)),
                ('lunch', models.TextField(blank=True)),
                ('snacks', models.TextField(blank=True)),
                ('dinner', models.TextField(blank=True)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mess', to='messmenu.Hostel')),
            ],
        ),
    ]
