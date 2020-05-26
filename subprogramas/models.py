from django.db import models
from django.core.validators import (
    MaxLengthValidator, MinLengthValidator,
    MinValueValidator, RegexValidator,
)
from programas.models import Programa
from usuarios.models import User


class Subprograma(models.Model):
    STATUS_CHOICES = (
        ('ACT', 'Activo'),
        ('INA', 'Inactivo')
    )
    programa = models.ForeignKey(
            Programa,
        verbose_name="Selecciona el programa",
            on_delete=models.CASCADE,
            blank=False,
            error_messages={
                "blank": "Debes indicar un programa.",
                "required": "Debes indicar un programa."
            }
        )

    nombre = models.CharField(
            max_length=50,
            unique=True,
            validators=[
                MinLengthValidator(
                    5, "El nombre debe ser de por lo menos 5 caracteres."),
                MaxLengthValidator(
                    50, "El nombre no puede pasar los 50 caracteres."),
                RegexValidator(
                    regex=r"^[A-Za-zÀ-ÿ\u00E0-\u00FC ]+$",
                    message="Solo se permiten letras.",
                    code="nombre_invalido"
                ),
            ], verbose_name="Nombre del Subprograma:",
            error_messages={
                "blank": "El nombre no puede estar vacío.",
                "required": "El nombre no puede estar vacío.",
                "unique": "Ya existe un subprograma con éste nombre"
            }
        )
    presupuesto = models.DecimalField(
            max_digits=15, decimal_places=3, blank=False,
            validators=[
                MinValueValidator(
                    0, "No puede tener valores negativos"),
            ],
            verbose_name="Presupuesto:",
            error_messages={
                "blank": "El presupuesto no puede estar vacío.",
                "invalid": "El presupuesto debe ser numérico."
            }
            # Recuerda:
            # https://docs.djangoproject.com/en/dev/ref/forms/fields/#error-messages
        )
    responsable = models.ForeignKey(
            User, verbose_name="Responsable:",
            on_delete=models.CASCADE,
            blank=False,
            error_messages={
                "blank": "Debes indicar un responsable.",
                "required": "Debes indicar un responsable."
            }
        )
    estatus = models.CharField(
        "Estatus Subprograma:", max_length=3,
        choices=STATUS_CHOICES, default='ACT'
    )

    def estatus_valor(self):
        return dict(Subprograma.STATUS_CHOICES)[self.estatus]

    def __str__(self):
        return self.nombre
