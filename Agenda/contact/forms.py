from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError

'''
3 maneiras de alterar o label de um campo no formulário:

1 - Definindo os campos diretamente na classe do formulário: No exemplo, 
o campo first_name é definido diretamente na classe ContactForm. Isso permite que 
você especifique o tipo de campo (neste caso, um CharField), 
o widget a ser usado (um TextInput), e quaisquer atributos adicionais para o widget 
(como classes CSS e um placeholder).

class ContactForm(forms.ModelForm):    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )
    
2 - Usando o método __init__ para alterar os atributos do widget: No método __init__, 
você pode atualizar os atributos do widget para um campo específico. 
Isso é útil se você quiser alterar os atributos com base em algum estado dinâmico ou 
condição. No exemplo, o código para fazer isso está comentado, mas se fosse descomentado, 
ele atualizaria os atributos do widget para o campo first_name.

 def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'classe-a classe-b',
            'placeholder': 'Aqui veio do init',
        })

3- Usando a classe Meta para alterar os widgets: Na classe Meta, você pode especificar 
um dicionário widgets para alterar o widget usado para um campo específico. Isso é
útil se você quiser alterar o widget para vários campos de uma vez, ou se você quiser 
manter a configuração do widget separada da definição do campo. No exemplo, 
o código para fazer isso também está comentado, mas se fosse descomentado, 
ele alteraria o widget para o campo first_name. Esse deve estar dentro do escopo 
da classe Meta.

widgets = {
    'first_name': forms.TextInput(
        attrs={
            'class': 'classe-a classe-b',
            'placeholder': 'Escreva aqui',
        }
    )
}
'''
class ContactForm(forms.ModelForm):
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'acept': 'image/*',
            }
            ),
    )
    
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category','picture',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )

        return first_name