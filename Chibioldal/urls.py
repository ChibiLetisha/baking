from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'recipe.views.home', name='home'),
    url(r'^recipe/(?P<id>\d+)', 'recipe.views.post', name='post'),
    url(r'^tip/(?P<id>\d+)', 'recipe.views.tip', name='specifictip'),
    url(r'^tips$', 'recipe.views.tips', name='tips'),
    url(r'^newtips$', 'recipe.views.newtips', name='newtips'),
    url(r'^mytips$', 'recipe.views.mytips', name='mytips'),
    url(r'^sharerecipes$', 'recipe.views.sharerecipes', name='sharerecipes'),
    url(r'^newrecipes$', 'recipe.views.newrecipes', name='newrecipes'),
    url(r'^myrecipes$', 'recipe.views.myrecipes', name='myrecipes'),
    url(r'^viewrecipes/(?P<id>\d+)', 'recipe.views.viewrecipes', name='viewrecipes'),
    url(r'^newestrecipes$', 'recipe.views.newestrecipes', name='newestrecipes'),
    url(r'search$', 'recipe.views.search', name='search'),
    url(r'login$', 'recipe.views.loguserin', name='login'),
    url(r'register', 'recipe.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),
)
