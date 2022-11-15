from django.urls import path
from .views import Homepage, Homefilmes, Detalhesfilme, Mostrar_eps
from .models import Filme, Episodio
from .models import Filme

# UMA URL, UMA VIEW E UM TEMPLATE

app_name = 'filme'


urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),  # Se colocar '/' no link final tem que colocar '//', porque ele já coloca '/' antes
    path(f'filmes/filme=<int:pk>/', Detalhesfilme.as_view(), name='detalhesfilme'),  # int:pk => um número inteiro que vai ser a primary key ( do banco de dados )
    path(f'filmes/filme=<int:filme_id>/episodio=<int:num_ep>/num_video=<int:pk>', Mostrar_eps.as_view(), name='mostrar_eps')
]

# path(f'filmes/<int:filme_id>/<num_ep>', Mostrar_eps.as_view(), name='mostrar_eps')
# No template:  <a href="{% url 'filme:mostrar_eps' episodio.filme_id episodio.num_ep %}"> <h1>Episodio {{forloop.counter}}: {{ episodio.titulo }} </h1> </a>
