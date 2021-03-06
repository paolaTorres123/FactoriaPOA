# Generated by Django 2.2.6 on 2019-12-03 03:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('primer_apellido', models.CharField(max_length=50, verbose_name='Primer apellido')),
                ('segundo_apellido', models.CharField(max_length=50, verbose_name='Segundo apellido')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='usuarios', verbose_name='Foto')),
                ('telefono', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]{10,10}$')], verbose_name='Teléfono')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
