import os
from os import getenv
from dotenv import load_dotenv
load_dotenv ()

import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'URL_Shortener_API_Core.settings')
django.setup()

from Accounts.models import Users  

def create_superuser():
    username = getenv('USERNAME')
    password = getenv('PASSWORD')
   

    if not Users.objects.filter(username=username).exists():
        Users.objects.create_superuser(username=username, password=password)
        print("Superuser created.")
    else:
        print("Superuser already exists.")

if __name__ == '__main__':
    create_superuser()
