from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'class': 'classe-a classe-b',
                'placeholder' : 'Aqui vai o primeiro nome'
            }
        ),
        label='Primeiro Nome',
        help_text= 'Help Text '
    )

    
    
    
    class Meta:
        
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
        
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
        
    def clean(self):
        
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 1',
                code='invalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        return super().clean()