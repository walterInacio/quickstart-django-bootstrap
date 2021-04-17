from django import forms

from .models import Esportes

class EsporteForm(forms.ModelForm):

    modalidade =forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    tipo =forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    distancia =forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': "form-control"}),
    )

    CHOICES= (
        ('M','Masculino'),
        ('F','Feminino'),
    )
    sexo =forms.CharField(
        max_length=1,
        widget=forms.Select(attrs={'class': "form-control"}, choices=CHOICES),
    )

    local =forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    class Meta:
        model = Esportes
        fields = ('modalidade', 'tipo', 'distancia', 'sexo', 'local')