from django.forms import ModelForm

from .models import Pune

class PuneForm(ModelForm):
    class Meta:
        model = Pune
        fields = ['title' , 'bio', 'location' , 'skills', 'perkohshmeri',
                'experience','pagesa' , 'orari']
