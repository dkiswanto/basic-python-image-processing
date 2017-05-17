from django.conf.urls import include, url

from . import views

app_name = 'rest_app'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/transform/$', views.transform),
]