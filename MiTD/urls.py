
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.home_page, name='home_page'),
    #url(r'^login/$', views.login_page, name='login'),
    #url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^torneos/', include('Apps.torneos.urls', namespace='torneos')),
    url(r'^usuario/', include('Apps.usuario.urls', namespace='usuario')),
    url(r'^$', login, {'template_name':'login.html'}, name='login'),
]