from django.forms import ModelForm, DateInput
from .models import Contato, Comentario
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContatoForm(ModelForm) :
    class Meta :
        model = Contato
        fields = '__all__'
        widgets = {
            'data_nascimento' : DateInput(attrs={'type' : 'date'})
        }


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ('clareza', 'originalidade','design', 'rigor','id', 'precisão', 'profundidade', 'amplitude', 'lógica', 'significância', 'classificação','comentário')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2' )







