from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ['nome', 'email', 'cpf']
		widgets = {
			'nome': forms.TextInput(attrs={'placeholder': 'Informe o nome do Cliente'}),
			'email': forms.TextInput(attrs={'placeholder': 'Informe o Email'}),
			'cpf': forms.TextInput(attrs={'placeholder': 'Informe o CPF'})
		}