from django.contrib import admin

# Register your models here.

from .models import Questao,Escolha

admin.site.register(Questao)
admin.site.register(Escolha)