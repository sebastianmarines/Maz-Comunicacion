# Generated by Django 3.0.2 on 2020-02-01 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodicos', '0002_auto_20200131_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='portadasycolumnas',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
