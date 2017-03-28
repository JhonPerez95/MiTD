from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Torneo

class Torneo_ListView(ListView):
    model = Torneo
    template_name = "torneos/torneo_listar.html"