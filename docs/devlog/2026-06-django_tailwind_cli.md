
# Reinício

# django_tailwind_cli

### 1. Biblioteca de estilo escolhida > tailwid 4...
O pacote django-tailwind-cli foi escolhido por ser uma solução madura que baixa e gerencia o executável (CLI) do Tailwind automaticamente.

```bash
pip install django-tailwind-cli
```

### 2. Configuração no settings.py
Duas alterações principais foram feitas no arquivo de configurações do projeto:
Registro do App: A biblioteca precisa ser incluída nos aplicativos instalados.

```bash
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    'django_tailwind_cli',
    'core',
]
```


Diretório de Arquivos Estáticos: O Django precisa saber onde procurar o arquivo CSS final gerado pelo Tailwind. O caminho apontado foi a raiz do projeto.

```bash
Python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```


### 3. Ajuste nos Templates
No seu arquivo de layout principal (base.html), as tags da biblioteca foram inseridas para puxar o CSS compilado.

 ```html
{% load tailwind_cli %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="UTF-8>
    <title>Document</title>
    {% tailwind_css %}
</head>
<body>
    {% block content %} {% endblock %}
</body>
</html>
```


### 4. Inicialização e Comandos do Terminal
Em vez do fluxo padrão do Django, o controle passa a ser feito pelos comandos integrados da ferramenta.
Comando de Setup: Executado apenas na primeira vez ou ao mudar de ambiente. Ele baixa o binário Standalone do Tailwind e cria a estrutura inicial do arquivo tailwind.css dentro da sua pasta static/css/.

```bash
python manage.py tailwind setup
```

Comando de Desenvolvimento: Substitui o runserver comum. Ele inicia o servidor do Django e, em paralelo no mesmo terminal, liga o compilador do Tailwind em modo de observação (watch). Isso garante que qualquer nova classe adicionada ao HTML seja injetada instantaneamente no CSS.

```bash
python manage.py tailwind runserver
```