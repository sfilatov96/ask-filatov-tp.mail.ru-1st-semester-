from django.conf.urls import patterns, include, url
from ask import views

urlpatterns = patterns('',
    url(r'^pip/', views.index, name='index'), 
    url(r'^$', views.index, name='index'),    	
)
