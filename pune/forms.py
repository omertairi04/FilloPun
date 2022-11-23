from django import forms

from .models import Pune

class PuneForm(forms.ModelForm):
    class Meta:
        model = Pune
        fields = ['title' , 'bio','image' ,'location' , 'skills', 'perkohshmeri',
                'experience','pagesa' , 'orari']

    def __init__(self , *args , **kwargs):
        super(PuneForm, self).__init__(*args, **kwargs)
        # ja ndryshon emrin e klases
#       self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
