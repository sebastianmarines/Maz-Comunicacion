# Generated by Django 3.0.2 on 2020-02-01 00:47

from django.db import migrations, models
import storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('periodicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portadasycolumnas',
            options={'verbose_name_plural': 'Portadas y Columnas'},
        ),
        migrations.AddField(
            model_name='portadasycolumnas',
            name='thumbnail',
            field=models.ImageField(blank=True, storage=storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]
