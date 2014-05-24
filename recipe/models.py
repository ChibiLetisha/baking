from django.contrib.auth.models import User
from django.db import models

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
