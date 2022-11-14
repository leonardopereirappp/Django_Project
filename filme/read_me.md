### Lembre-se: <u>Cada página</u> do seu site tem:
* Uma url
* Um view
* Um template

<hr>

# No views.py:

#### Temos um GRANDE dilema aqui: usar Function Based View ou Class Based View? (Dá uma olhada no link abaixo)
#### ==> https://www.geeksforgeeks.org/class-based-vs-function-based-views-which-one-is-better-to-use-in-django/ <==

## FBV  =>  função que gerencia as views
* Para sites mais simples, esse modelo serviria
* Temos a desvantagem de ter que fazer todas as funções do absoluto zero
* Mas a vantagem de ter funções do jeito que queremos sem seguir modelo pré-definido

## Exemplo de FBV:
<pre>
def homepage(request):
    return render(request, 'homepage.html')
</pre>

<hr>

## CBV  =>  classe que gerencia as views
* Para sites mais robustos e que precisam de objetos próprios
* Temos algumas vantagens como: já tem muita estrutura do próprio Django própria (não precisa criar do zero)
* Com a desvantagem de não ter algo 100% seu (customizado)
## Exemplo de CBV:
<pre>
from django.views.generic import TemplateView
class Homepage(TemplateView):
    template_name = 'homepage.html'
</pre>

<hr>

##### No caso do nosso site, decidimos por usar o CBV certo? Mas não tem certo nem errado, só escolhe um e vai na fé :)

<hr>

# No urls.py

<h5> Mudar de: </h5>

<pre>
urlpatterns = [
    path('', homepage),
]
</pre>
<h5> Para: </h5>
<pre>
urlpatterns = [
    path('', Homepage.as_view()),
]
</pre>
