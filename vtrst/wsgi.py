"""
WSGI config for vtrst project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv, find_dotenv

# load enviroment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), 'settings/.env')
load_dotenv(dotenv_path)

application = get_wsgi_application()
