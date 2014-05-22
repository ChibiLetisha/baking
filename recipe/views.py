from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from recipe.forms import TipForm
from recipe.models import Recipe, Category, Tip


def home(request):
    blogs = Recipe.objects.all().order_by("-date")[:9]
    categories = Category.objects.all().order_by("name")
    return render(request, "index.html", {"blogs": blogs, "categories":categories})

def post(request, id):
    blog = get_object_or_404(Recipe, pk=id)
    return render(request, "post.html", {"recipe": blog})

def tips(request):
    tips = Tip.objects.all().order_by("-date")
    categories = Category.objects.all().order_by("name")
    return render(request, "tips.html", {"tips": tips, "categories": categories})

def tip(request, id):
    tip = get_object_or_404(Tip, pk=id)
    categories = Category.objects.all().order_by("name")
    return render(request, "tip.html", {"tip": tip, "categories": categories})

@login_required
def newtips(request):
    newtip = TipForm()
    if request.method == 'POST':
        newtip = TipForm(request.POST)
        if newtip.is_valid():
            nt=newtip.save()
            nt.user=request.user
            nt.save()
            return HttpResponseRedirect('/tips')
    categories = Category.objects.all().order_by("name")
    return render(request, "newtips.html",{"newtips": newtip, "categories": categories})

def mytips(request):
    tips = Tip.objects.filter(user=request.user).order_by("-date")
    categories = Category.objects.all().order_by("name")
    return render(request, "tips.html", {"tips": tips, "categories": categories})