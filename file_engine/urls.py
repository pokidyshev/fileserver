from django.conf.urls import url

from file_engine.views import home, upload


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^upload/$', upload, name='upload'),
]
