# Generated by Django 4.1.1 on 2022-11-30 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0006_alter_rutina_completado_alter_rutina_ejercicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grabacion',
            name='nombre',
        ),
    ]
