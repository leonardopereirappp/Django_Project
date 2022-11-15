from django.shortcuts import render
from .models import Filme, Episodio
from django.views.generic import TemplateView, CreateView, ListView, DetailView
import pandas as pd

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


class Mostrar_eps(DetailView):  # Retorna um object -> 1 item do nosso modelo de cada vez
    template_name = "mostrar_eps.html"
    model = Episodio
    context_object_name = "mostrar_eps"

    def get(self, request, *args, **kwargs):
        # Salvar a quantidade de views na tabela de episódio (quantidade de view de cada vídeo)
        episodio = self.get_object()   # Descobrir qual ao filme que está acessando
        episodio.visualizacoes_ep += 1   # Somar um nas visualizações do filme
        episodio.save()   # Salvando as alterações, é tipo um commit()
        # Salvar a quantidade de views total de cada série
        self.model = Filme
        filme = self.get_object()  # Descobrir qual ao filme que está acessando
        filme.visualizacoes += 1  # Somar um nas visualizações do filme
        filme.save()  # Salvando as alterações, é tipo um commit()
        return super().get(request, *args, **kwargs)  # Redireciona para a url final

    def get_context_data(self, **kwargs):
        context = super(Mostrar_eps, self).get_context_data(**kwargs)
        eps = Episodio.objects.filter(id=self.get_object().id)[0]
        context['episodio'] = eps
        return context


