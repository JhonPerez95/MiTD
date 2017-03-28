from django.conf.urls import url
from .views import User_CreateView


urlpatterns = [
    url(r'^registrar/$', User_CreateView.as_view(), name='registrar'),
]