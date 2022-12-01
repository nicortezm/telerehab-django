# Generated by Django 4.1.1 on 2022-12-01 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0014_alter_comentario_rutina_alter_feedback_rutina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='rutina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagina.rutina'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rutina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagina.rutina'),
        ),
    ]
