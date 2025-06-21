# +++++++++++ DJANGO +++++++++++
# To use your own Django app use code like this:
from django.core.wsgi import get_wsgi_application
import os
import sys

# assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/hreinosoflores/django-blog'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog_enterprise.settings'

# Uncomment the lines below depending on your Django version
# then, for Django >=1.5:
application = get_wsgi_application()
# or, for older Django <=1.4
# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()
