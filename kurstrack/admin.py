from django.contrib import admin

# Register your models here.
#from kurstrack.models import *
from django.apps import apps

app = apps.get_app_config('kurstrack')

for model_name, model in app.models.items():
    admin.site.register(model)