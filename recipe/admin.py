from django.contrib import admin
from recipe.models import Recipe, Category, Tip, UserProfile, RecipeComments, TipComments

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Tip)
admin.site.register(UserProfile)
admin.site.register(RecipeComments)
admin.site.register(TipComments)