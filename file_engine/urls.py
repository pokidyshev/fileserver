from django.conf.urls import url

from file_engine import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^[0-9a-zA-Z]+$', views.details, name='details')
]
