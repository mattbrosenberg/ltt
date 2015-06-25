from django.forms import ModelForm
from .models import Libor

class LiborForm(ModelForm):
    class Meta:
        model = Libor
        fields = ['date', 'rate']