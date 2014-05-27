# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from recipe.models import Tip, Category, Recipe, UserProfile, RecipeComments, TipComments


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
        fields = ['title', 'post', 'category', 'picture']

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    user_name = forms.CharField(label=u"Felhasználó név", max_length=50)
    e_mail = forms.EmailField(label=u"E-mail cím")
    password = forms.CharField(label=u"Jelszó", max_length=50, widget=forms.PasswordInput)
    password_again = forms.CharField(label=u"Jelszó megerősítése", max_length=50, widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label="Vezetéknév", max_length=30)
    last_name = forms.CharField(label="Keresztnév", max_length=30)

    class Meta:
        model = User
        fields = ["first_name", "last_name"]

class UserProfileForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput)
    class Meta:
        model = UserProfile
        fields = ["birth_date", "bio", "gender", "avatar", "user"]

class RecipeCommentForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput)
    recipe = forms.CharField(widget=forms.HiddenInput)
    class Meta:
        model = RecipeComments

    def clean(self):
        cleaned_data = super(RecipeCommentForm, self).clean()
        cleaned_data['user'] = User.objects.get(pk=cleaned_data.get('user'))
        cleaned_data['recipe'] = Recipe.objects.get(pk=cleaned_data.get('recipe'))
        return cleaned_data

class TipCommentForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput)
    tip = forms.CharField(widget=forms.HiddenInput)
    class Meta:
        model = TipComments

    def clean(self):
        cleaned_data = super(TipCommentForm, self).clean()
        cleaned_data['user'] = User.objects.get(pk=cleaned_data.get('user'))
        cleaned_data['tip'] = Tip.objects.get(pk=cleaned_data.get('tip'))
        return cleaned_data
