from django.contrib import admin
from recipe.models import Recipe, Category, Tip

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Tip)