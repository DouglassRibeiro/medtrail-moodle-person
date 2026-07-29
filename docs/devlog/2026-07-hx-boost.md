# Aplica uma SPA de forma progracisava

# Possibilita uma entrada ao histórico

# hx-boost oferece um controle mais granular

## 1. context_processors.py para expor a variável HTMX_ENABLED para todos os tampletes.
```python
from django.conf import settings

def htmx_context(request):
    return {
        'HTMX_ENABLED': getattr(settings, 'HTMX_ENABLED', True),
    }

```
## 2. settings.py adicione 'config.context_processors.htmx_context', informando o novo processador de contexto ao django
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'config.context_processors.htmx_context', # Adicione esta linha informando o novo processador de contexto ao django
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


### Ativando ou desativando o HTMX globalmente
```python 
# HTMX Configuration
HTMX_ENABLED = True # Defina como False para desativar o HTMX globalmente e forçar recarregamentos completos
```


## 3. Já na base.html organize seu caminho 
```html
    <script src="{% static 'js/htmx.min.js' %}"></script>
</head>

<body {% if HTMX_ENABLED %}class="htmx-enabled"{% endif %}> {# Opcional: Adiciona uma classe para estilização ou JS #}
    <div id="main-content" {% if HTMX_ENABLED %}hx-boost="true" hx-target="#main-content" hx-swap="innerHTML settle:300ms"{% endif %}>
        {% block content %} {% endblock %}
    </div>

</body>
```

## É crucial que todos os links de navegação tenham um href válido. Se o HTMX estiver desativado, o navegador usará o href para a navegação padrão. Se o HTMX estiver ativado (via hx-boost no pai), ele interceptará o href. O hx-get no primeiro link se torna redundante quando hx-boost está ativo e o href já aponta para a URL correta.

```html
    <div class="-z-10 absolute inset-0 bg-cover bg-center bg-no-repeat blur-sm scale-105"
        style="background-image: url('{% static 'core/img/Image_2ljwx32ljwx32ljw.webp' %}');">
    </div>
    <section class="relative p-8 grid place-items-center h-screen">
        <div class="lg:flex sm:flex grid p-4 rounded-2xl min-w-auto min-h-auto">
            <a href="{% url 'accounts:login' %}" hx-target="#main-content" class="lg:mr-20 mb-10 sm:mr-10 sm:mb-0 lg:m-0 text-center content-center text-white border-0 p-4 rounded-2xl w-40 h-20 font-bold backdrop-blur-3xl shadow-[0px_0px_16px_8px_rgba(0,0,0,0.50)] hover:shadow-[0px_0px_16px_8px_rgba(0,0,0,0.80)] hover:-translate-y-0.5 hover:scale-105 active:scale-95 active:translate-y-0 transition-all duration-300">Entrar</a>
            <a href="{% url 'accounts:register' %}" hx-target="#main-content" hx-swap="innerHTML settle:300ms" class="lg:ml-20 mt-10 sm:ml-10 sm:mt-0 lg:m-0 text-center content-center text-white border-0 p-4 rounded-2xl w-40 h-20 font-bold backdrop-blur-3xl shadow-[0px_0px_16px_8px_rgba(0,0,0,0.50)] hover:hadow-[0px_0px_16px_8px_rgba(0,0,0,0.80)] hover:-translate-y-0.5 hover:scale-105 active:scale-95 active:translate-y-0 transition-all duration-300">Registrar</a>
        </div>
    </section>
  
</main>
{% endblock %}
```
## O formulário também precisa de um action válido para quando o HTMX estiver desativado.
```html
{% load static %}

{% block content %}
<form hx-target="#main-content" class="flex flex-col items-center justify-center w-96 h-96" action="{% url 'accounts:login' %}" method="post"> {# Adicione um action e method apropriados #}
    <input class="bg-white m-6" type="text" name="none" placeholder="Digite seu nome">
    <input type="number" name="idade" placeholder="Digite sua idade">
</form>
{% endblock %}

```