from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from .models import Torneo, Equipo
from .forms import Torneo_Form, Equipo_Form


class Torneo_CreateView(CreateView):
	model = Torneo
	form_class = Torneo_Form
	template_name = "torneos/torneo_crear.html"
	success_url = reverse_lazy('torneos:torneo_listar')

	def form_valid(self, form_class):
		form_class.instance.user_id = self.request.user.id
		return super(Torneo_CreateView, self).form_valid(form_class) 


class Torneo_ListView(ListView):    
	template_name = 'torneos/torneo_listar.html'

	def get_queryset(self, *args, **kwargs):
		return Torneo.objects.filter(user=self.request.user)

class Torneo_DetailView(DetailView):
	model = Torneo
	template_name = "torneos/torneo_detalle.html"


class Equipo_CreateView(CreateView):
	model = Equipo
	template_name = "torneos/equipo_crear.html"
	form_class = Equipo_Form
	success_url = reverse_lazy('torneos:equipo_crear')

	def get_form_kwargs(self):
		kwargs = super(Equipo_CreateView, self).get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

	def form_valid(self, form_class):
		form_class.instance.user_id = self.request.user.id
		return super(Equipo_CreateView, self).form_valid(form_class)