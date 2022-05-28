from django.urls import include,re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   url(r'^$', views.index, name='index'),
    url(r'^gallery$', views.gallery, name='gallery'),
]