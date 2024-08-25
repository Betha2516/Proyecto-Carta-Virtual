from django.contrib import admin
from .models import  Entrada, PlatoF, Bebida, Postre, Ubicaciones

# Register your models here.
admin.site.register(Entrada)
admin.site.register(PlatoF)
admin.site.register(Bebida)
admin.site.register(Postre)
admin.site.register(Ubicaciones)