from django import forms
from .models import Contato, Usuario

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto','mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu email'}),
            'mensagem': forms.Textarea(attrs={'placeholder': 'Digite sua mensagem'}),
        }

    OPCOES_ASSUNTO = [
        ('', 'Escolha uma opção'),
        ('DUVIDAS', 'Dúvidas/informações'),
        ('SOLICITACOES', 'Solicitações'),
        ('ELOGIOS', 'Elogios'),
        ('SUGESTOES', 'Sugestões'),
        ('RECLAMACOES', 'Reclamações')
    ]
    assunto = forms.ChoiceField(choices=OPCOES_ASSUNTO)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu email'}),
            'senha': forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
            }