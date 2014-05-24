from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from recipe.forms import TipForm, RecipeForm, LoginForm, Register
from recipe.models import Recipe, Category, Tip


def home(request):
    blogs = Recipe.objects.all().order_by("-date")[:9]
    categories = Category.objects.all().order_by("name")
    return render(request, "index.html", {"blogs": blogs, "categories":categories})

def post(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    return render(request, "post.html", {"recipe": recipe})

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

@login_required
def mytips(request):
    tips = Tip.objects.filter(user=request.user).order_by("-date")
    categories = Category.objects.all().order_by("name")
    return render(request, "tips.html", {"tips": tips, "categories": categories})

@login_required
def sharerecipes(request):
    recipes = Recipe.objects.all().order_by("-date")
    categories = Category.objects.all().order_by("name")
    return render(request, "sharerecipes.html", {"recipes": recipes, "categories": categories})

@login_required
def newrecipes(request):
    newrecipe = RecipeForm()
    if request.method == 'POST':
        newrecipe = RecipeForm(request.POST)
        if newrecipe.is_valid():
            nt=newrecipe.save()
            nt.user=request.user
            nt.save()
            return HttpResponseRedirect('/sharerecipes')
    categories = Category.objects.all().order_by("name")
    return render(request, "newrecipes.html",{"newrecipes": newrecipe, "categories": categories})

@login_required
def myrecipes(request):
    recipes = Recipe.objects.filter(user=request.user).order_by("-date")
    categories = Category.objects.all().order_by("name")
    return render(request, "sharerecipes.html", {"recipes": recipes, "categories": categories})

def viewrecipes(request, id):
    recipes = Recipe.objects.filter(category=Category.objects.get(pk=id)).order_by("-date")
    categories = Category.objects.all().order_by("name")
    return render(request, "sharerecipes.html", {"recipes": recipes, "categories": categories})

def newestrecipes(request):
    recipes = Recipe.objects.all().order_by("-date")[:6]
    categories = Category.objects.all().order_by("name")
    return render(request, "sharerecipes.html", {"recipes": recipes, "categories":categories})

def search(request):
    recipes = Recipe.objects.filter(Q(title__contains=request.GET["Kereses"]) | Q(post__contains=request.GET["Kereses"]))
    categories = Category.objects.all().order_by("name")
    return render(request, "sharerecipes.html", {"recipes": recipes, "categories":categories})

def loguserin(request):
    loginform = LoginForm()
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            user = authenticate(username=request.POST["user_name"], password=request.POST["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/sharerecipes')
    categories = Category.objects.all().order_by("name")
    return render(request, "login.html", {"loginform": loginform, "categories":categories})

def register(request):
    register = Register()
    if request.method == 'POST':
        register = Register(request.POST)
        if register.is_valid():
            User.objects.create_user(request.POST["user_name"], request.POST["e_mail"], request.POST["password"])
            return HttpResponseRedirect('/login')
    categories = Category.objects.all().order_by("name")
    return render(request, "login.html", {"loginform": register, "categories":categories})
