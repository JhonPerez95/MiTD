
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

from .views import User_CreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^torneos/', include('Apps.torneos.urls', namespace='torneos')),
    url(r'^registrar/$', User_CreateView.as_view(), name='registrar'),
    url(r'^accounts/login/', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/',  logout_then_login, name='logout')
]