# Generated by Django 3.0.7 on 2021-06-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AddField(
            model_name='orders',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
    ]
