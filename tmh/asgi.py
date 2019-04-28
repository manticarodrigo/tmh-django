import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tmh.config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

django.setup()
application = get_default_application()
