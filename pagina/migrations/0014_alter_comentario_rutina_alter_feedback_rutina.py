# Generated by Django 4.1.1 on 2022-11-30 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0013_rename_comentario_comentario_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='rutina',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pagina.rutina'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rutina',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pagina.rutina'),
        ),
    ]