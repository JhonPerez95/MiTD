from django.conf.urls import url
from django.contrib.auth.decorators import login_required 

from .views import Torneo_ListView , Torneo_CreateView, Torneo_DetailView, Equipo_CreateView


urlpatterns = [
    url(r'^listar/$', login_required(Torneo_ListView.as_view()), name='torneo_listar'),
    url(r'^crear/$', login_required(Torneo_CreateView.as_view()), name='torneo_crear'),
    url(r'^detalle/(?P<pk>\d+)/$', login_required(Torneo_DetailView.as_view()), name='torneo_detalle'),
    url(r'^equipo/$', login_required(Equipo_CreateView.as_view()), name='equipo_crear'),
]
