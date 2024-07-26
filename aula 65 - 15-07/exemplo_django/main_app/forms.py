from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto','mensagem']

    OPCOES_ASSUNTO = [
        ('', 'Escolha uma opção'),
        ('DUVIDAS', 'Dúvidas/informações'),
        ('SOLICITACOES', 'Solicitações'),
        ('ELOGIOS', 'Elogios'),
        ('SUGESTOES', 'Sugestões'),
        ('RECLAMACOES', 'Reclamações')
    ]
    assunto = forms.ChoiceField(choices=OPCOES_ASSUNTO)
    
    def clean_categoria(self):
        data = self.cleaned_data['assunto']
        if data == '':
            raise forms.ValidationError("Este campo é obrigatório.")
        return data
        