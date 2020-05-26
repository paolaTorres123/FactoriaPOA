from django.contrib import admin
from .models import Programa, Partida, MetaPrograma, MetaReal
# Register your models here.

admin.site.register(Programa)
admin.site.register(Partida)
admin.site.register(MetaPrograma)
admin.site.register(MetaReal)
