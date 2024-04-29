from django.contrib import admin
from .models import Category, Note
# Register your models here.

models = [Category, Note]
admin.site.register(models)
 