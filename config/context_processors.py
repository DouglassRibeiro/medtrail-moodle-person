from django.conf import settings

def htmx_context(request):
    return {
        'HTMX_ENABLED': getattr(settings, 'HTMX_ENABLED', True),
    }