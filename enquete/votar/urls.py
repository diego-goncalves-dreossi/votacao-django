from django.urls import path
"""
- path() é a função para criar uma url de um projeto, ela fica dentro da cosntante urlpatterns em urls.py.
- path tem 2 parâmetros, o nome da url e o que irá acontecer, para onde irá, uma função que informará a 
lógica do sistema, e podemos colocar um name, que facilita chamadas.
"""
from . import views
app_name = 'votar'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:questao_id>/resultados/',views.resultados,name='resultados'),
    path('<int:questao_id>/vote/',views.vote,name='vote')
]

# path('<int:questao_id>/',views.detalhe,name='detalhe'),