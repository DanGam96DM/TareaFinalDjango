from django.conf.urls import url
from . import views
urlpatterns = [
    #url(r'^$', views.lista_eventos, name ='lista_eventos'),
    url(r'^evento/nuevo/$', views.evento_nuevo, name='evento_nuevo'),
]
