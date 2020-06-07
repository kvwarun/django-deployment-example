from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^new/',views.newextension,name='new'),
    url(r'^second/',views.secondextension,name='second'),
]
