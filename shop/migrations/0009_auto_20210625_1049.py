# Generated by Django 3.0.7 on 2021-06-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210624_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=30000),
        ),
    ]
