"""
WSGI config for URL_Shortener_API_Core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from URL_Shortener_API_Core.create_superuser_deploy import create_superuser

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'URL_Shortener_API_Core.settings')

create_superuser()
application = get_wsgi_application()


