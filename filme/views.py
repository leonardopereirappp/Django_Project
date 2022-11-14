from django.shortcuts import render
from .models import Filme, Episodio
from django.views.generic import TemplateView, CreateView, ListView, DetailView

# Create your views here.

# UMA URL, UMA VIEW E UM TEMPLATE

class Homepage(TemplateView):  # Visualizar o template ( HTML )
    template_name = 'homepage.html'

class Homefilmes(ListView):  # Retorna um object-list -> lista de itens do modelo
    template_name = "homefilmes.html"
    model = Filme
    context_object_name = "lista_filmes"

class Detalhesfilme(DetailView):  # Retorna um object -> 1 item do nosso modelo de cada vez
    template_name = "detalhesfilme.html"
    model = Filme
    context_object_name = "filme"

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:15]
        context['filmes_relacionados'] = filmes_relacionados
        return context



class Mostrar_eps(DetailView):
    template_name = 'mostrar_eps.html'
    model = Episodio
    context_object_name = 'episodio'

    def get_context_data(self, **kwargs):
        contexto = super(Mostrar_eps, self).get_context_data(**kwargs)
        episodios = Episodio.objects.filter(filme_id=self.get_object().filme)
        contexto['episodios'] = episodios
        return contexto
