# -*- coding: utf-8 -*-

from django import forms
from recipe.models import Tip, Category


class TipForm(forms.ModelForm):
    title = forms.CharField(label=u"Cím")
    post = forms.CharField(label=u"Leírás", widget=forms.Textarea())
    category = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all(),
    label=u"Kategória")

    class Meta:
        model = Tip
        fields = ['title', 'post', 'category']
