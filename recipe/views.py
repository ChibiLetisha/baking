from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from recipe.forms import TipForm, RecipeForm, LoginForm, RegisterForm, UserProfileForm, UserForm, RecipeCommentForm, \
    TipCommentForm
from recipe.models import Recipe, Category, Tip, UserProfile, RecipeComments, TipComments


def home(request):
    blogs = Recipe.objects.all().order_by("-date")[:9]
    categories = Category.objects.all().order_by("name")
    return render(request, "index.html", {"blogs": blogs, "categories":categories})

def post(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    categories = Category.objects.all().order_by("name")
    comments = RecipeComments.objects.filter(recipe=recipe)
    commentform = RecipeCommentForm(initial={'user':request.user.pk, 'recipe':recipe.pk})
    if request.method == 'POST':
        commentform = RecipeCommentForm(request.POST)
        if commentform.is_valid():
            commentform.save()
            commentform = RecipeCommentForm(initial={'user':request.user.pk, 'recipe':recipe.pk})
    return render(request, "post.html", {"recipe": recipe, "categories":categories, "comments":comments, "commentform":commentform})


def tips(request):
    tips = Tip.objects.all().order_by("-date")
    categories = Category.objects.all().order_by("name")
    return render(request, "tips.html", {"tips": tips, "categories": categories})

def tip(request, id):
    tip = get_object_or_404(Tip, pk=id)
    categories = Category.objects.all().order_by("name")
    comments = TipComments.objects.filter(tip=tip)
    commentform = TipCommentForm(initial={'user':request.user.pk, 'tip':tip.pk})
    if request.method == 'POST':
        commentform = TipCommentForm(request.POST)
        if commentform.is_valid():
            commentform.save()
            commentform = TipCommentForm(initial={'user':request.user.pk, 'tip':tip.pk})
    return render(request, "tip.html", {"tip": tip, "categories": categories, "comments":comments, "commentform":commentform})

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
def deletetip(request, id):
    try:
        tip = Tip.objects.get(pk=id)
        tip.delete()
    except:
        return HttpResponse(status=404)
    return HttpResponseRedirect(reverse("tips"))

@login_required
def mytipcomments(request):
    tipcomments =TipComments.objects.filter(user=request.user).order_by("-date")
    categories = Category.objects.all().order_by("name")
    return render(request, "mytipcomments.html", {"tipcomments": tipcomments, "categories": categories})

@login_required
def deletetipcomment(request, id):
    try:
        tipcomment = TipComments.objects.get(pk=id)
        tipcomment.delete()
    except:
        return HttpResponse(status=404)
    return HttpResponseRedirect(reverse("mytipcomments"))

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

@login_required
def deleterecipe(request, id):
    try:
        recipe = Recipe.objects.get(pk=id, user=request.user)
        recipe.delete()
    except:
        return HttpResponse(status=404)
    return HttpResponseRedirect(reverse("sharerecipes"))

@login_required
def myrecipecomments(request):
    recipecomments = RecipeComments.objects.filter(user=request.user).order_by("-date")
    categories = Category.objects.all().order_by("name")
    return render(request, "myrecipecomments.html", {"recipecomments": recipecomments, "categories": categories})

@login_required
def deleterecipecomment(request, id):
    try:
        recipecomment = RecipeComments.objects.get(pk=id)
        recipecomment.delete()
    except:
        return HttpResponse(status=404)
    return HttpResponseRedirect(reverse("myrecipecomments"))

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
    register = RegisterForm()
    if request.method == 'POST':
        register = RegisterForm(request.POST)
        if register.is_valid():
            if request.POST["password"] == request.POST["password_again"]:
                u = User.objects.create_user(request.POST["user_name"], request.POST["e_mail"], request.POST["password"])
                up = UserProfile.objects.create(user=u)
                up.save()
                return HttpResponseRedirect('/login')
    categories = Category.objects.all().order_by("name")
    return render(request, "login.html", {"loginform": register, "categories":categories})

def loguserout(request):
    logout(request)
    return HttpResponseRedirect('/')


def handle_uploaded_file(f):
    destination = open('somefilename.png', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()


def profil(request):
    user_profil = UserProfileForm(instance=UserProfile.objects.get(user=request.user))
    user = UserForm(instance=request.user)
    if request.method == 'POST':
        user_profil = UserProfileForm(request.POST, request.FILES, instance=UserProfile.objects.get(user=request.user))
        user = UserForm(request.POST, instance=request.user)
        if user_profil.is_valid() and user.is_valid():
            handle_uploaded_file(request.FILES['avatar'])
            user_profil.save()
            user.save()
    categories = Category.objects.all().order_by("name")
    return render(request, "profil.html", {"UserProfile":user_profil, "User": user, "categories":categories})