# Generated by Django 4.1.1 on 2022-10-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_remove_actividad_kinesiologo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejercicio',
            name='video_thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
