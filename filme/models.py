from django.db import models
from django.utils import timezone

# Create your models here.
# Aqui se cria as tabelas do banco de dados

# Criar o filme

#  -> Filmes/séries [episódios[videos, titulo], quantidade_views, data_criação, thumb, titulo, descrição, categoria]

# Crie fora da classe a lista de categorias em que cada categoria é uma tupla assim: (armazenar_no_bd, aparecer_para_o_usuario)
LISTA_CATEGORIAS = ( ("PROGRAMAÇÃO", "PROGRAMAÇÃO".capitalize()), ("APRESENTAÇÕES", "APRESENTAÇÕES".capitalize()), ("ANÁLISES", "ANÁLISES".capitalize()), ("OUTROS", "OUTROS".capitalize()) )
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    # Na categoria, vamos separar em 3: programação: (python,vba, sql), apresentações(power_point) e análises (excel, power_bi)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):  # Essa função diz para cada classe do .py, qual o formato de string que ela tem que fazer com cada objeto criado a partir dessa classe. Que por padrão seria algo do tipo: 'Filme object (1)'
        return self.titulo


# Criar os episódios

class Episodio(models.Model):
    filme = models.ForeignKey(to="Filme", related_name="episodios", on_delete=models.CASCADE)  #  Aqui é a chave estrangeira do model Filme
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    num_ep = models.IntegerField(default=0)
    visualizacoes_ep = models.IntegerField(default=0)

    def __str__(self):  # Só pra não ficar um Episodio.object no database
        return f"{self.filme.titulo} (Ep. {self.num_ep}) - {self.titulo}"




# Criar os usuários (DJANGO já tem uma estrutura pronta para isso, então meio que não é necessário)
