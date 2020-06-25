from django import forms

from .models import Games


PLATAFORMS_CHOICES = (
    ('Nintendo DS', 'Nintendo DS'),
    ('Nintendo Switch', 'Nintendo Switch'),
    ('Playstation 3', 'Playstation 3'),
    ('Playstation 4', 'Playstation 4'),
    ('Xbox 360', 'Xbox 360'),
    ('Xbox One', 'Xbox One'),
)

class GameForm(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=200)

    price = forms.DecimalField(
        label='Preço', max_digits=10, decimal_places=2,
        widget=forms.TextInput)

    main_photo = forms.ImageField(label='Foto')

    plataforms = forms.MultipleChoiceField(
        label='Plataformas',
        widget=forms.CheckboxSelectMultiple,
        choices=PLATAFORMS_CHOICES)

    class Meta:
        model = Games
        fields = ('name',)
