from django.urls import include,re_path as url
from . import views
from unicodedata import name
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^gallery$', views.gallery, name='gallery'),
   url(r'^search/', views.search_category, name = 'search_category')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)