# Esse arquivo é um gerenciador de contexto ( todas as páginas HTML vão ter acesso ao contexto que criarmos aqui )

from .models import Filme, Episodio

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')
    return {'lista_filmes_recentes': lista_filmes}

def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')
    return {'lista_filmes_em_alta': lista_filmes}

def lista_episodios(request):
    lista_eps = Episodio.objects.all().order_by('filme_id')
    return {'lista_eps': lista_eps}

