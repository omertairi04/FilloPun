from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Pune , Apliko
from .forms import PuneForm

def kerkoPune(request):
    pune = Pune.objects.all()

    context = {
        'pune':pune,
        
    }
    return render(request , 'pune/kerkopune.html',context)

@login_required(login_url='login')
def shpallPune(request):
    profile = request.user.profile
    form = PuneForm()
    
    if request.method == 'POST':
        form = PuneForm(request.POST , request.FILES)
        if form.is_valid():
            pune = form.save(commit=False)
            pune.business = profile
            pune.save()
            form.save_m2m()
            
            return redirect('kerko-pune')

    context = {
        'form':form
    }
    return render(request , 'pune/shpallpune.html',context)

@login_required(login_url='login')
def singlePune(request , pk):
    profile = request.user.profile
    pune = Pune.objects.get(id=pk)

    context = {
        'pune':pune,
    }
    return render(request , 'pune/single-pune.html', context)

@login_required(login_url='login')
def apliko(request , pk):
    user = request.user
    pune = Pune.objects.get(id=pk)
    current_aplicants = pune.aplicants
    has_apliku = Apliko.objects.filter(user=user , post=pune).count()
    if not has_apliku:
        has_apliku = Apliko.objects.create(user=user , post=pune)
        current_aplicants = current_aplicants + 1
    else:
        has_apliku = Apliko.objects.filter(user=user , post=pune).delete()
        current_aplicants = current_aplicants - 1
    pune.aplicants = current_aplicants
    pune.save()

    next = request.GET['next'] if 'next' in request.GET else '/kerko-pune/'

    return HttpResponseRedirect(next)
