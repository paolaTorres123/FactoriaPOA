from django.forms import ModelForm, CharField, PasswordInput
from django.forms import ValidationError, TextInput, CheckboxInput
from django.forms import BooleanField, FileInput
from django.contrib.auth.models import User
from usuarios.models import Administrativo
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
import re

PASSWORD_INCORRECTO = "La contraseña no sigue el formato solicitado: 8"
PASSWORD_INCORRECTO += " - 50 caracteres mínimo (una mayúscula, una "
PASSWORD_INCORRECTO += "minúscula, un número y un símbolo)."

USERNAME_INVALIDO = "El nombre de usuario no sigue el formato solicitado, "
USERNAME_INVALIDO += "favor de verificarlo."

password_validator = RegexValidator(
    "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[$@$!%*?&._-])"
    + "([A-Za-z\\d$@$!%*?&]|[^ ]){8,50}$",
    PASSWORD_INCORRECTO)
username_validator = RegexValidator("^[a-zA-Z]{8,20}$", USERNAME_INVALIDO)


class UserForm(ModelForm):

    password = CharField(widget=PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Escribe contraseña'}),
        label='Contraseña',
        validators=[password_validator])
    password_re = CharField(widget=PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Repite contraseña'}),
        label='Confirmación de contraseña',
        validators=[password_validator])
    username = CharField(widget=TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Nombre de usuario'}),
        label='Nombre de usuario',
        error_messages={'required':
                        'El nombre de usuario es requerido,'
                        + ' favor de completarlo.'},
        validators=[username_validator])
    email = CharField(widget=TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Correo electrónico'}),
        label='Correo electrónico',
        error_messages={'invalid':
                        'Favor de ingresar un formato de correo válido.',
                        'required':
                        'El correo es requerido, favor de completarlo.'})
    is_superuser = BooleanField(widget=CheckboxInput(),
                                label="¿Es director operativo?",
                                required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'password_re', 'is_superuser']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_password_re(self, **kwargs):
        if self.data['password_re'].find(" ") > 0:
            raise ValidationError(PASSWORD_INCORRECTO)
        if self.data['password_re'] != self.data['password']:
            raise ValidationError("Las contraseñas no coinciden.")
        return self.data['password_re']

    def clean_username(self):
        username = self.data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError(
                "El usuario ingresado ya se encuentra registrado en el"
                + " sistema, favor de verificarlo.")
        if len(username) > 20:
            raise ValidationError(
                "El nombre de usuario debe contener máximo 20 caracteres.")
        if len(username) < 8:
            raise ValidationError(
                "El nombre de usuario debe contener mínimo 8 caracteres.")
        if not self.data['username']:
            raise ValidationError(
                "El nombre de usuario es requerido, favor de completarlo.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError(
                "El correo electrónico ingresado ya se encuentra "
                + "registrado en el sistema. Favor de verificarlo.")
        return email


class AdministrativoForm(ModelForm):
    class Meta:
        model = Administrativo
        exclude = ['usuario']

        error_messages = {
            'nombre': {
                'required':
                'El nombre es requerido, favor de completarlo.',
                'max_length':
                'La longitud máxima del nombre es de 50 caracteres.'
            },
            'primer_apellido': {
                'required':
                'El primer apellido es requerido, favor de completarlo.',
                'max_length':
                'La longitud máxima del primer apellido es de 50 caracteres.'
            },
            'segundo_apellido': {
                'max_length':
                'La longitud máxima del segundo apellido es de 50 caracteres.'
            },
            'telefono': {
                'invalid': 'El formato del número telefónico es inválido'
            },
        }

        widgets = {
            'nombre': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'primer_apellido': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Primer apellido'}),
            'segundo_apellido': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Segundo apellido'}),
            'telefono': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'foto': FileInput(
                attrs={'class': 'form-control', 'placeholder': 'Fotografía'}),
        }

    def clean_telefono(self):
        tel = self.cleaned_data['telefono']
        pattern = re.compile("^[0-9]{10,10}$")
        if not pattern.match(tel):
            raise ValidationError(
                "El número telefónico debe contener 10 dígitos.")
        return tel


class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(
        {'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = CharField(
        widget=PasswordInput(
            {'class': 'form-control', 'placeholder': 'Contraseña'}),
        error_messages={'required':
                        'La contraseña es requerida, favor de verificarla.'})

    class Meta:
        fields = '__all__'

    error_messages = {
        'invalid_login': _(
            "El usuario o la contraseña son incorrectos,"
            + " favor de intentarlo nuevamente."
        ),
    }
