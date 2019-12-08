from django.forms import ModelForm 
from . models import Pessoa, Veiculo, Movimento_Rotativo, Mensalista, MovMensalista, Marca
from django import forms
import datetime




class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'        


class Mov_RotativoForm(ModelForm):
    class Meta:
        model = Movimento_Rotativo
        fields = '__all__'
       

class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'




class Mov_MensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'

      
        

'''
class Mov_RotativoForm(ModelForm):
    class Meta:
        model = Movimento_Rotativo
        fields = '__all__'
        fields = ['checkin']  
        checkin = forms.DateField(widget=forms.DateTimeField())
        widgets = { 'checkin': DateInput()}

'''