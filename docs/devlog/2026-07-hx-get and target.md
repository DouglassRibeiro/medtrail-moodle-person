# hx-get={"% url'...' %"} = interage como um href porém sem substituir toda a pagina, e sim fazendo uma requisição AJAX em segundo plano trazendo um recarregamento parcial.

```htmx
    hx-get="{% url 'accounts:login' %}"
```
---

# hx-target={} garante o carregamento total seguindo outras definições de estilo, garantindo que apenas a seção desejada seja atualizada.

```htmx
    hx-target="#main-content"
```

# Conclusão
## O id="main-content" (ou um elemento com um ID ou classe similar que sirva como alvo principal) é essencial para que o HTMX realizar a troca de conteúdo parcial de forma controlada e eficiente, proporcionando a experiência de "Single Page Application". Sem ele, o HTMX não teria um ponto de referência claro para onde injetar as respostas do servidor, o que por fim recarregaria a página por completo.

```html
{% load tailwind_cli %}
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    {% tailwind_css %}
    <script src="{% static 'js/htmx.min.js' %}"></script>
</head>

<body>
    <div id="main-content">
        {% block content %} {% endblock %}
    </div>

</body>
</html>
```