from django.contrib import admin
from recipe.models import Recipe, Category

admin.site.register(Recipe)
admin.site.register(Category)