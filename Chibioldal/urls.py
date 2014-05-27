from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'recipe.views.home', name='home'),
    url(r'^recipe/(?P<id>\d+)', 'recipe.views.post', name='post'),
    url(r'^tip/(?P<id>\d+)', 'recipe.views.tip', name='specifictip'),
    url(r'^tips$', 'recipe.views.tips', name='tips'),
    url(r'^newtips$', 'recipe.views.newtips', name='newtips'),
    url(r'^mytips$', 'recipe.views.mytips', name='mytips'),
    url(r'^deletetip/(?P<id>\d+)', 'recipe.views.deletetip', name='deletetip'),
    url(r'^mytipcomments$', 'recipe.views.mytipcomments', name='mytipcomments'),
    url(r'^deletetipcomment/(?P<id>\d+)', 'recipe.views.deletetipcomment', name='deletetipcomment'),
    url(r'^deleterecipecomment/(?P<id>\d+)', 'recipe.views.deleterecipecomment', name='deleterecipecomment'),
    url(r'^sharerecipes$', 'recipe.views.sharerecipes', name='sharerecipes'),
    url(r'^newrecipes$', 'recipe.views.newrecipes', name='newrecipes'),
    url(r'^myrecipecomments$', 'recipe.views.myrecipecomments', name='myrecipecomments'),
    url(r'^myrecipes$', 'recipe.views.myrecipes', name='myrecipes'),
    url(r'^viewrecipes/(?P<id>\d+)', 'recipe.views.viewrecipes', name='viewrecipes'),
    url(r'^deleterecipe/(?P<id>\d+)', 'recipe.views.deleterecipe', name='deleterecipe'),
    url(r'^newestrecipes$', 'recipe.views.newestrecipes', name='newestrecipes'),
    url(r'^search$', 'recipe.views.search', name='search'),
    url(r'^login$', 'recipe.views.loguserin', name='login'),
    url(r'^register', 'recipe.views.register', name='register'),
    url(r'^logout', 'recipe.views.loguserout', name='logout'),
    url(r'^profil', 'recipe.views.profil', name='profil'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
