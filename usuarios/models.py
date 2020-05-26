from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (RegexValidator,
                                    MinLengthValidator, MaxLengthValidator,
                                    FileExtensionValidator)
from django.core.exceptions import ValidationError
import re


class Administrativo(models.Model):
    nombre = models.CharField("Nombre", max_length=50, validators=[
        MinLengthValidator(
            3, "La longitud mínima del nombre es de 3 caracteres."),
        MaxLengthValidator(
            50, "La longitud máxima del nombre es de 50 caracteres."),
        RegexValidator('^([A-ZÁÉÍÓÚ]{1}[a-zñáéíóú]+[\\s]*)+$',
                       "Formato de nombre incorrecto, favor de veriicarlo.",)],
        error_messages={
            'required': "El nombre es requerido, favor de completarlo."}
    )
    primer_apellido = models.CharField(
        "Primer apellido", max_length=50,
        validators=[
            MinLengthValidator(
                3,
                "La longitud mínima del primer apellido es de 3 caracteres."),
            MaxLengthValidator(
                50,
                "La longitud máxima del primer apellido es de 50 caracteres."),
            RegexValidator('^([A-ZÁÉÍÓÚ]{1}[a-zñáéíóú]+[\\s]*)+$',
                           "Formato del primer apellido incorrecto,"
                           + " favor de veriicarlo.")
        ])
    segundo_apellido = models.CharField(
        "Segundo apellido", max_length=50, blank=True, validators=[
            MinLengthValidator(
                3,
                "La longitud mínima del segundo apellido es de 3 caracteres."
            ),
            MaxLengthValidator(
                50,
                "La longitud máxima del segundo apellido es de 50 caracteres."
            ),
            RegexValidator('^([A-ZÁÉÍÓÚ]{1}[a-zñáéíóú]+[\\s]*)+$',
                           "Formato del segundo apellido incorrecto,"
                           + " favor de veriicarlo.")
        ])
    foto = models.ImageField(
        'Foto', upload_to='usuarios',  blank=True,  null=True, validators=[
            FileExtensionValidator(['png', 'jpeg', 'jpg'],
                                   "Formato de imagen inválido.")
        ])
    telefono = models.CharField("Teléfono", max_length=10, validators=[
        RegexValidator('^[0-9]{10,10}$',
                       "Formato del número de teléfono incorrecto."),
        MinLengthValidator(
            10, "El número telefónico debe contener 10 dígitos."),
        MaxLengthValidator(
            10, "El número telefónico debe contener 10 dígitos."),
    ])
    usuario = models.OneToOneField(
        User, verbose_name="Usuario", on_delete=models.CASCADE,
        error_messages={
            'required': "El usuario es requerida, favor de indicar sus datos."
            })

    def clean(self):
        pattern = re.compile("^[a-zA-Z]{8,20}$")
        count = 0
        dic = {'username': [], 'email': [], 'password': []}
        try:
            if not self.usuario.username:
                dic['username'].append('El usuario es requerido.')
                count += 1
            if not pattern.match(self.usuario.username):
                dic['username'].append(
                    'El nombre de usuario no sigue el formato solicitado,'
                    + ' favor de verificarlo.')
                count += 1
            if not self.usuario.email or not self.usuario.email.strip():
                dic['email'].append('El correo electrónico es requerido.')
                count += 1
        except Exception:
            count = 0

        if count > 0:
            raise ValidationError(dic)

    def __str__(self):
        return self.nombre + ' ' + self.primer_apellido
