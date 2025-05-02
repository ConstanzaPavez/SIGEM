from django import forms
from .models import Articulo, Miembro, Solicitud

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'cantidad', 'estado', 'tipo_dano', 'imagen']


class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['nombre', 'rol', 'experiencia_previa', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'rol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rol actual'}),
            'experiencia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Experiencia anterior', 'rows': 3}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        } 