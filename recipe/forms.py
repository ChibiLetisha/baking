# -*- coding: utf-8 -*-

from django import forms
from recipe.models import Tip, Category, Recipe


class TipForm(forms.ModelForm):
    title = forms.CharField(label=u"Cím")
    post = forms.CharField(label=u"Leírás", widget=forms.Textarea())
    category = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all(),
    label=u"Kategória")

    class Meta:
        model = Tip
        fields = ['title', 'post', 'category']

class RecipeForm(forms.ModelForm):
    title = forms.CharField(label=u"Cím")
    post = forms.CharField(label=u"Leírás", widget=forms.Textarea())
    category = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all(),
    label=u"Kategória")

    class Meta:
        model = Recipe
        fields = ['title', 'post', 'category']

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class Register(forms.Form):
    user_name = forms.CharField(max_length=50)
    e_mail = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)