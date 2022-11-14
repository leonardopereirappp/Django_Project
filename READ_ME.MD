# DJANGO é um framework em python que possibilita criarmos sites, sendo o .py no back e html/css/js no front-end
# Nesse projeto faremos uma cópia da netflix, claro com um banco de dados diferente do da empresa
# E como não tenho um time de desenvolvedores, mas sou só eu, eu não pretendo fazer o projeto de forma profissional, mas sim para portfólio

# FLASK vs DJANGO

# """

# O DJANGO tem toda uma estrutura pronta, você tem que utilizá-la dessa forma para o site/API/micro-serviço funcionar
# Já começa de forma pesada, mas com o tempo se pega tudo que tu faz ali

# O FLASK é mais simples de começar, utilizado em projetos pequenos, como API's simples.

# Mas lembrando que não tem melhor ou pior, isso depende da necessidade de cada empresa/instituição

# """

# nome = "Nome"
# Antes de começarmos, para começarmos as configs:
f"""
# pip install django
# 'django-admin startproject {nome} .'
"""
# O . serve para não criarmos uma pasta nome com uma subpasta nome, e sim somente a subpasta com o manage.py


# Com essas etapas feita, tu pode rodar um 
#    'python manage.py runserver'
# no terminal para ver o começo da sua jornada

# Depois dessas etapas, basta criar a pasta que contenha as partes do seu site
# nome_app = "batata"
# f'Depois dessas etapas prontas: django-admin startapp {nome_app}'


# Para criarmos o SuperUser (alguém que terá acesso ao {link_server}/admin ) rode os códigos:
# (1° Rodada do código) -> 'python manage.py makemigrations' (para adicionar coisas no seu banco de dados)
# (1° Rodada do código) -> 'python manage.py migrate' (para atualizar o seu banco de dados)
# (Se não é a primeira rodada, é essa etapa aqui) -> 'python manage.py createsuperuser'
# Preencha com os dados e ao terminar, tu terá acesso ao {link_server}/admin

# site = 'https://docs.djangoproject.com/en/3.2/ref/django-admin/'
# f'Qualquer dúvida sobre algo: {site}'

# Agora iremos vincular o app com o projeto inicial
# f'Para instalar o app nos apps padrão do projeto, precisamos ir em {nome}/settings.py e acrescentar uma linha em INSTALLED_APPS'
# Obs: para ver o nome do app, é só ir na pasta do app e procurar pelo arquivo apps.py, que tu encontra facilmente o name

# Agora, tu tem que ir no arquivo urls.py e definir qual o link que quer que seja exibido

# Tu pode adicionar de duas formas, usar o urls.py do projeto principal, ou criar um url em cada app e no arquivo principal importar todas as configs

# Vou preferir usar a segunda opção como forma de esteticamente o código ficar menos poluído

# f'Agora, vá no {nome}/setting.py e altere o TIME_ZONE e LANGUAGE_CODE'

# O próximo passo foi criar a categoria filmes lá no filme/models e fazer aquelas duas etapas do banco de dados

# Após isso, temos de ir no filme/admin e adicionar a tabela criada para ir no {link}/admin e termos acesso

# Assim:

# from .models import CLASSNAME
# admin.site.register(CLASSNAME)

# Agora acessa o site: https://docs.djangoproject.com/en/4.1/howto/static-files/ e faça essas configurações

# Para definir os links da url. Ex.: /images do => https://google.com/images, temos que ir nos urls e definir

