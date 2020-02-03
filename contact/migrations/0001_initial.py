# Generated by Django 3.0.2 on 2020-02-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('sub_coah', models.BooleanField()),
                ('sub_nl', models.BooleanField()),
                ('sub_mex', models.BooleanField()),
                ('message', models.TextField()),
            ],
        ),
    ]