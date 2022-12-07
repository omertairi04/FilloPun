from django.shortcuts import render

from users.models import Profile , Skills
from pune.models import Pune

def Home(request):
    context = {


    }

    return render(request , 'home.html', context)
