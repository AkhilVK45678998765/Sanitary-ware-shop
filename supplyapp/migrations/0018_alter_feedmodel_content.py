# Generated by Django 4.1.5 on 2023-02-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplyapp', '0017_feedmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedmodel',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]