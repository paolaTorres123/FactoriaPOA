from django.db import models
from django.core.validators import (MaxLengthValidator, MaxValueValidator,
                                    MinValueValidator,
                                    MinLengthValidator)
from django.core.validators import RegexValidator
# Create your models here.
LONGITUD_MAXIMA = 'Error de longitud'
LONGITUD_MINIMA = 'Error de longitud mínima'
VALOR_MINIMO = 'El valor mínimo permitido es 0'
VALOR_MAXIMO = 'El valor máximo permitido son 6000000'
formato_numero = 'El formato del año fiscal es incorrecto,'
formato_numero += ' debe ser indicado con un número de 4 dígitos'
FORMATO_NUMERO_INCORRECTO = formato_numero
NPARI = "Formato del nombre de la partida es incorrecto, favor de verificarlo."
numero_actividad_in = "El formato del número de actividades es incorrecto,"
numero_actividad_in += " debe ser indicado con un número"
NUMERO_ACTIVIDAD_INCORRECTO = numero_actividad_in
numero_bene_in = "El formato del número de beneficiario es incorrecto,"
numero_bene_in += " debe ser indicado con un número"
NUMERO_BENEFICIA_INCORRECTO = numero_bene_in
programa_inc = "Formato del nombre del programa es incorrecto,"
programa_inc += " favor de verificarlo."
FORMATO_NOMBRE_P = programa_inc
formato_fuente = "Formato de la fuente del programa es incorrecto,"
formato_fuente += " favor de verificarlo."
FORMATO_FUENTE_INC = formato_fuente


class Partida(models.Model):
    numero_partida = models.IntegerField(default=0, validators=[
        RegexValidator(
            r'^[0-9]{4,4}$',
            "El número de partida debe de contener 4 dígitos."),
    ])  # 3000,
    nombre_partida = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='',
        validators=[
            RegexValidator(
                r'^[a-zA-zÁÉÍÓÚñáéíóúÑ][a-zA-z ÁÉÍÓÚñáéíóúÑ]+$',
                NPARI),
            MaxLengthValidator(
                70, LONGITUD_MAXIMA),
            MinLengthValidator(
                5, LONGITUD_MINIMA),
        ])
    monto_partida = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0,
        validators=[
            MinValueValidator(
                0, VALOR_MINIMO),
            MaxValueValidator(
                6000000, VALOR_MAXIMO)
        ])  # 6700.00
    # Implementación de internet
    programa = models.ForeignKey(
        'Programa',
        related_name="partidas",
        on_delete=models.CASCADE,
        default=''
    )

    def __str__(self):
        return self.nombre_partida


class MetaPrograma(models.Model):
    EDAD_CHOICES = (
        ('NAD', 'Niños y Adolescentes (11-17 años)'),
        ('JOV', 'Jóvenes (18 a 29 años)'),
        ('ADU', 'Adultos (30+ años)')
    )
    numero_actividades = models.IntegerField(
        "No. Actividades:",
        default=0,
        validators=[
            MinValueValidator(
                0, VALOR_MINIMO),
            MaxValueValidator(
                100,
                NUMERO_ACTIVIDAD_INCORRECTO)
        ])
    numero_beneficiarios = models.IntegerField(
        "Beneficiarios:",
        default=0,
        validators=[
            MinValueValidator(
                0, VALOR_MINIMO),
            MaxValueValidator(
                9000000, NUMERO_BENEFICIA_INCORRECTO)
        ])
    numero_hombres = models.IntegerField("Hombres:", default=0, validators=[
        MinValueValidator(0, VALOR_MINIMO),
        MaxValueValidator(9000000, VALOR_MAXIMO)
    ])
    numero_mujeres = models.IntegerField("Mujeres:", default=0, validators=[
        MinValueValidator(0, VALOR_MINIMO),
        MaxValueValidator(9000000, VALOR_MAXIMO)
    ])
    edad = models.CharField("Rango:", max_length=3,
                            choices=EDAD_CHOICES, default='')
    meta_esperada = models.BooleanField(default=True)

    programa = models.ForeignKey(
        'Programa', related_name="metas", on_delete=models.CASCADE, default=''
    )

    def __str__(self):
        return "{} - {}".format(self.numero_beneficiarios, self.numero_mujeres)


class MetaReal(models.Model):
    EDAD_CHOICES = (
        ('NAD', 'Niños y Adolescentes (11-17 años)'),
        ('JOV', 'Jóvenes (18 a 29 años)'),
        ('ADU', 'Adultos (30+ años)')
    )
    numero_actividades_r = models.IntegerField(
        "No. Actividades:",
        default=0,
        validators=[
            MinValueValidator(
                0, VALOR_MINIMO),
            MaxValueValidator(
                100, NUMERO_ACTIVIDAD_INCORRECTO)
        ])
    numero_beneficiarios_r = models.IntegerField(
        "Beneficiarios:",
        default=0,
        validators=[
            MinValueValidator(
                0, VALOR_MINIMO),
            MaxValueValidator(
                9000000, NUMERO_BENEFICIA_INCORRECTO)
        ])
    numero_hombres_r = models.IntegerField("Hombres:", default=0, validators=[
        MinValueValidator(0, VALOR_MINIMO),
        MaxValueValidator(9000000, VALOR_MAXIMO)
    ])
    numero_mujeres_r = models.IntegerField("Mujeres:", default=0, validators=[
        MinValueValidator(0, VALOR_MINIMO),
        MaxValueValidator(9000000, VALOR_MAXIMO)
    ])
    edad_r = models.CharField("Rango:", max_length=3,
                              choices=EDAD_CHOICES, default='')
    meta_esperada_r = models.BooleanField(default=True)

    programa_r = models.ForeignKey(
        'Programa',
        related_name="metas_r",
        on_delete=models.CASCADE,
        default=''
    )

    def __str__(self):
        return "{} - {}".format(
            self.numero_beneficiarios_r,
            self.numero_mujeres_r)


class Programa(models.Model):
    # attbs del Modelo Programa
    TIPO_CHOICES = (
        ('MEN', 'Mensual'),
        ('BIM', 'Bimestral'),
        ('TRI', 'Trimestral'),
    )

    STATUS_CHOICES = (
        ('ACT', 'Activo'),
        ('INA', 'Inactivo')
    )

    EDAD_CHOICES = (
        ('NAD', 'Niños y Adolescentes (11-17 años)'),
        ('JOV', 'Jóvenes (18 a 29 años)'),
        ('ADU', 'Adultos (30+ años)')
    )

    TIPO_PROGRAMA_PRES = (
        ('APO', 'Apoyo'),
        ('SER', 'Servicio'),
        ('FOM', 'Fomento'),
    )

    nombre = models.CharField(
        "Nombre del programa:",
        max_length=100,
        null=False,
        blank=False,
        default='',
        validators=[
            MaxLengthValidator(100, LONGITUD_MAXIMA),
            MinLengthValidator(5, LONGITUD_MINIMA),
            RegexValidator(
                r'^[a-zA-zÁÉÍÓÚñáéíóúÑ][a-zA-z ÁÉÍÓÚñáéíóúÑ]+$',
                FORMATO_NOMBRE_P)
        ])

    anio_ejercicio_fiscal = models.IntegerField(
        "Año Fiscal:",
        default=0,
        validators=[
            RegexValidator(
                r'^[0-9]{4,4}$',
                "El año fiscal debe de contener 4 dígitos."
            ),
        ])
    recurso_asignado = models.DecimalField(
        "Recurso Asignado:",
        max_digits=9,
        decimal_places=2,
        default=0,
        validators=[
            MinValueValidator(0, VALOR_MINIMO),
            MaxValueValidator(6000000, VALOR_MAXIMO)])
    fuente = models.CharField(
        "Fuente:",
        default='',
        max_length=100,
        validators=[
            RegexValidator(
                r'^[a-zA-zÁÉÍÓÚñáéíóúÑ][a-zA-z ÁÉÍÓÚñáéíóúÑ]+$',
                FORMATO_FUENTE_INC
            ),
            MaxLengthValidator(100, LONGITUD_MAXIMA),
            MinLengthValidator(5, LONGITUD_MINIMA),
        ])
    tipo = models.CharField("Tipo de Apoyo:", max_length=3,
                            choices=TIPO_CHOICES, default='')
    status = models.CharField(
        "Estatus Programa:", max_length=3, choices=STATUS_CHOICES, default='')
    tipo_programa_p = models.CharField(
        "Tipo de Programa Presupuestario:",
        max_length=3,
        null=False,
        blank=False,
        default='',
        choices=TIPO_PROGRAMA_PRES)

    # tipo_programa_presupuestario
    def __str__(self):
        return "{} - {}".format(self.nombre, self.anio_ejercicio_fiscal)

    def return_nombre(self):
        return self.nombre
