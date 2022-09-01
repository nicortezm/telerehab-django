from django.shortcuts import render

# Create your views here.


def is_kinesiologo(user):
    return user.groups.filter(name='KINESIOLOGO').exists()


def is_paciente(user):
    # retorna True si el usuario es PACIENTE y false en todos los otros casos
    return user.groups.filter(name='PACIENTE').exists()
