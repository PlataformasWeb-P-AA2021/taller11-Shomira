from django.forms import ModelForm
from django.forms.widgets import Textarea
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
       Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese dirección por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
            'tipo': _('Ingrese el tipo de edificio'),

        }
    
 
    '''Agregar validaciones'''
    '''El nombre de la ciudad no puede iniciar con la letra mayúscula L'''

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'numero_cuartos', 'edificio']
        labels = {
                'nombre_propietario': _('Ingrese nombre del propietario por favor'),
                'costo': _('Ingrese el costo por favor'),
                'numero_cuartos': _('Ingrese el numero de cuartos por favor'),
                'edificio': _('Elija un edificio'),
    

            }
    #Costo de un departamento no puede ser mayor a $100 mil.
    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 100:
            raise forms.ValidationError("Costo Excesivo")
        return valor	
class EdificioDepartamentoForm(ModelForm): 
   
    #args tupla de opciones **kwarsg diccionario
    
    def __init__(self, edificio, *args, **kwargs):
    #Constructor que hace referencia al self para sobreescribir el
    #constructor de model form
        super(EdificioDepartamentoForm, self).__init__(*args, **kwargs)
        # darle un valor inicial a ese atributo
        # le asigna unn edificio y lo crea como hidden o oculto
        # se agrega el objeto departamento asociada
        self.initial['edificio'] = edificio
        # darle a edificio un widget que hace generar un forms
        # para generar un input oculto
        self.fields['edificio'].widget = forms.widgets.HiddenInput()

    
    class Meta:
        model = Departamento 
        fields = ['nombre_propietario','costo','numero_cuartos', 'edificio'] 



