from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto','mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu email', 'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'placeholder': 'Digite sua mensagem', 'class': 'form-control'}),
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
    
        