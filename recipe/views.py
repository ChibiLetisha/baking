from django.shortcuts import render, get_object_or_404

# Create your views here.
from recipe.models import Recipe


def home(request):
    blogs = Recipe.objects.all().order_by("-date")
    return render(request, "index.html", {"blogs": blogs})

def post(request, id):
    blog = get_object_or_404(Recipe, pk=id)
    return render(request, "post.html", {"recipe": blog})

