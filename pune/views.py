from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Pune

def kerkoPune(request):
    pune = Pune.objects.all()

    context = {
        'pune':pune,
    }
    return render(request , 'pune/kerkopune.html',context)

@login_required(login_url='login')
def apliko(request):
    pass
