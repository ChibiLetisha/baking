from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    post = models.TextField("Description")
    date = models.DateTimeField()
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title
