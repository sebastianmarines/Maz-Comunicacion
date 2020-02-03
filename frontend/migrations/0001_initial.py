# Generated by Django 3.0.2 on 2020-02-03 21:24

from django.db import migrations, models
import storage_backends


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default='MAZ Comunicación', max_length=100)),
                ('sub_header', models.CharField(default='Estrategia y Publicidad', max_length=200)),
                ('image', models.ImageField(storage=storage_backends.PublicMediaStorage(), upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
