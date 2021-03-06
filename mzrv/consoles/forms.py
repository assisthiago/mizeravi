from django import forms

from .models import Consoles


PLATAFORMS_CHOICES = (
    ('Microsoft', 'Microsoft'),
    ('Nintendo', 'Nintendo'),
    ('Playstation', 'Playstation'),
)

class ConsoleForm(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=200)

    price = forms.DecimalField(
        label='Preço', max_digits=10, decimal_places=2,
        widget=forms.TextInput)

    main_photo = forms.ImageField(label='Foto')

    plataforms = forms.MultipleChoiceField(
        label='Plataforma',
        widget=forms.CheckboxSelectMultiple,
        choices=PLATAFORMS_CHOICES)

    class Meta:
        model = Consoles
        fields = (
            'name',
            'price',
            'main_photo',
            'plataforms',
        )
