from django import forms

from .models import Accessories


PLATAFORM_CHOICES = (
    ('', 'Escolha uma opção'),
    ('Microsoft', 'Microsoft'),
    ('Nintendo', 'Nintendo'),
    ('Playstation', 'Playstation'),
)

class AccessoryForm(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=200)

    price = forms.DecimalField(
        label='Preço', max_digits=10, decimal_places=2,
        widget=forms.TextInput)

    main_photo = forms.ImageField(label='Foto')

    plataform = forms.ChoiceField(
        label='Plataforma',
        choices=PLATAFORM_CHOICES)

    class Meta:
        model = Accessories
        fields = (
            'name',
            'price',
            'main_photo',
            'plataform',
        )
