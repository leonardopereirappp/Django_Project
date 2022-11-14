# Filmes/séries
* quantidade_views,
* data_criação,
* thumb,
* titulo,
* descrição,
* categoria

#  Episódios
* A qual filme esse ep faz referência (Foreign Key do model acima (Filme))
* videos (link do vídeo (Youtube no caso))
* titulo

<hr>

## Lembrando que a cada mudança no banco de dados:
### * python manage.py makemigrations 
### * python manage.py migrate

#### Depois de cada tabela criada, é importante ir no admin.py e adicionar a tabela criada, para visualizar na página do /admin