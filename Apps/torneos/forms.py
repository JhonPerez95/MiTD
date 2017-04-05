from django import forms 
from .models import Torneo, Equipo
from colorful.fields import RGBColorField

class Torneo_Form(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = [
        	'descripcion',
        ]	

        labels={
        	'descripcion':'Nombre Torneo',
        }

        widgets={
        	'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }

class Equipo_Form(forms.ModelForm):
    class Meta:
        model = Equipo
        fields =[
            'nombre',
            'color',
            'torneo',
        ]

        labels={
            'nombre':'Nombre del Equipo',
            'color':'Color Uniforme',
            'torneo':'Participar Torneo',
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'color': RGBColorField(),
            'torneo': forms.Select(attrs={'class':'form-control'}),
        }
        