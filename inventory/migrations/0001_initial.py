# Generated by Django 2.0.1 on 2018-01-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_name', models.CharField(max_length=140)),
                ('notes', models.TextField()),
            ],
        ),
    ]
