# Generated by Django 3.1.12 on 2022-08-17 11:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0038_auto_20210606_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('numproducts', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('str_id', models.CharField(editable=False, max_length=58, null=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, default='')),
                ('brand', models.CharField(blank=True, default='', max_length=60)),
                ('warranty', models.BooleanField(default=False)),
                ('packaging', models.BooleanField(default=False)),
                ('condition', models.CharField(choices=[('1', '01/10'), ('2', '02/10'), ('3', '03/10'), ('4', '04/10'), ('5', '05/10'), ('6', '06/10'), ('7', '07/10'), ('8', '08/10'), ('9', '09/10'), ('10', '10/10')], default='7', max_length=2)),
                ('action', models.CharField(choices=[('sell', 'Sell'), ('giveaway', 'Give Away'), ('rent', 'Rent')], default='sell', max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=100)),
                ('negotiable', models.BooleanField(default=True)),
                ('contact_details', models.CharField(max_length=300)),
                ('time_of_creation', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='buyandsell.category')),
                ('followers', models.ManyToManyField(blank=True, related_name='_product_followers_+', to='users.UserProfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-time_of_creation',),
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('addressed', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyandsell.product')),
                ('reporter', models.ForeignKey(on_delete=models.SET('User_DNE'), to='users.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endtime', models.DateTimeField()),
                ('strikes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ImageURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyandsell.product')),
            ],
        ),
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endtime', models.DateTimeField()),
                ('user', models.ManyToManyField(to='users.UserProfile')),
            ],
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['time_of_creation'], name='buyandsell__time_of_5c6bcd_idx'),
        ),
    ]
