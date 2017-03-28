from django.conf.urls import url
from .views import Torneo_ListView

urlpatterns = [
    url(r'^listar/$', Torneo_ListView.as_view(), name='torneo_listar'),
]
