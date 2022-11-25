from django.forms import ModelForm 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile , Skills , Message

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']
        labels = {
            'first_name':'Name', # qysh del nform!
        }

    def __init__(self , *args , **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # ja ndryshon emrin e klases
#       self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','sur_name','email','username','profilepic',
                'bio','skills' ,'CV','resume' ,'birth_date','location']

    def __init__(self , *args , **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # ja ndryshon emrin e klases
#       self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']

    def __init__(self , *args , **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        # ja ndryshon emrin e klases
#       self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

