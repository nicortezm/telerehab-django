# Generated by Django 4.1.1 on 2022-11-30 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0012_alter_comentario_rutina_alter_feedback_rutina'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='comentario',
            new_name='texto',
        ),
    ]
