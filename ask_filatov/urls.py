"""ask_filatov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from ask import views


urlpatterns = [
    url(r'^profile/edit',views.profile,name='profile'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^question/(?P<qnum>\d+)/(?P<page>\d+)?/?', views.question, name='question'),
    url(r'^tag/(?P<tag>\w+)/(?P<page>\d+)?/?', views.tag, name='tag'),
    #url(r'^ask/', include('ask.urls')),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^hot/(?P<page>\d+)?/?', views.hot, name='hot'),
    url(r'^register/$', views.register, name='register'),
    url(r'^ask/$', views.ask, name='ask'),
    #url(r'^index1/', views.index1, name='index1'),
    url(r'^(?P<page>\d+)?/?', views.index, name='index'),

    
   

    
    	
]
