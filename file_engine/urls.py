from django.conf.urls import url

from file_engine import views


urlpatterns = [
    url(r'^$', views.upload, name='upload'),
    url(r'^[2-9a-hj-km-np-z]+$', views.details, name='details'),
    url(r'^download/[2-9a-hj-km-np-z]+$', views.download, name='download'),
]
