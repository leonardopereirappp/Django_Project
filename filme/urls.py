from django.urls import path
from .views import Homepage, Homefilmes, Detalhesfilme, Mostrar_eps
from .models import Filme

# UMA URL, UMA VIEW E UM TEMPLATE

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),  # Se colocar '/' no link final tem que colocar '//', porque ele já coloca '/' antes
    path(f'filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),  # int:pk => um número inteiro que vai ser a primary key ( do banco de dados )
    path(f'filmes/<int:filme_id>/<int:pk>/', Mostrar_eps.as_view(), name='mostrar_eps')
]
