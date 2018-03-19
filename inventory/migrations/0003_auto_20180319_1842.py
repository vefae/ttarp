# Generated by Django 2.0.1 on 2018-03-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20180319_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='package_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='reorder_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='unit',
            field=models.CharField(default=1, max_length=140),
            preserve_default=False,
        ),
    ]