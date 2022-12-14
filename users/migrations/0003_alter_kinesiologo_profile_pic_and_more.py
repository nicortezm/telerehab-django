# Generated by Django 4.1 on 2022-09-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_kinesiologo_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kinesiologo',
            name='profile_pic',
            field=models.ImageField(default='profile_pic/default.png', upload_to='profile_pic/kinesiologo/', verbose_name='Foto de perfil'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='profile_pic',
            field=models.ImageField(default='profile_pic/default.png', upload_to='profile_pic/paciente/', verbose_name='Foto de perfil'),
        ),
    ]
