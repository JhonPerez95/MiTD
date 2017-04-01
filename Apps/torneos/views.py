from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView 	
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from .models import Torneo
from .forms import TorneoForm

class Torneo_ListView(ListView):    
    template_name = 'torneos/torneo_listar.html'

    def get_queryset(self, *args, **kwargs):
        return Torneo.objects.filter(user=self.request.user)



class Torneo_CreateView(CreateView):
    model = Torneo
    form_class = TorneoForm
    template_name = "torneos/torneo_crear.html"
    succes_url = reverse_lazy('torneos:torneo_listar')
