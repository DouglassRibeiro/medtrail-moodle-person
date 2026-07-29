from django.conf import settings

def htmx_context(request): # HTMX contexto
    return {
        'HTMX_ENABLED': getattr(settings, 'HTMX_ENABLED', True),
    }