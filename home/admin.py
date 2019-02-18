from django.contrib import admin

# Register your models here.

from django.apps import apps

# Register your models here.
apps_list = apps.get_app_config('home').get_models()

for model in apps_list:
    admin.site.register(model)
