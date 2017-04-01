from django import forms 
from .models import Torneo

class TorneoForm(forms.ModelForm):
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
        