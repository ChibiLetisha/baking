# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

GENDER = (
    (True, u"Nő"),
    (False, u"Férfi")
)

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    post = models.TextField("Description")
    date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, null=True, blank=True)
    picture = models.ImageField(upload_to="Pictures/", null=True, blank=True)

    def __unicode__(self):
        return self.title

class Tip(models.Model):
    title = models.CharField(max_length=255)
    post = models.TextField("Description")
    date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birth_date = models.DateField(u"Születési dátum", null=True, blank=True)
    gender = models.NullBooleanField(u"Nem", null=True, blank=True, choices=GENDER)
    bio = models.TextField(u"Magamról", null=True, blank=True)
    avatar = models.ImageField(u"Kép", upload_to="Avatars/", null=True, blank=True)

    def __unicode__(self):
        return self.user.username

class RecipeComments(models.Model):
    user = models.ForeignKey(User)
    post = models.TextField("Komment")
    date = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe)

class TipComments(models.Model):
    user = models.ForeignKey(User)
    post = models.TextField("Komment")
    date = models.DateTimeField(auto_now_add=True)
    tip = models.ForeignKey(Tip)
