from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User

from .forms import UserRegisterForm , EditProfileForm
from .models import Profile

def profile(request , username):
    profile = Profile.objects.get(username=username)
    skills = profile.skills.all()
    context = {
        'profile':profile,
        'skills':skills
    }
    return render(request , 'users/profile.html', context)

def editProfile(request):
    profile = request.user.profile
    form = EditProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST , request.FILES , instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile' , username = profile.username)
        
    context = {
        'profile':profile,
        'form':form
    }

    return render(request , 'users/edit-account.html', context)

def registerUser(request):
    page = 'user'
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # messages

            login(request , user)
            return redirect('editProfile')
        else:
            pass

    context = {
        'page':page,
        'form':form,
    }
    return render(request , 'users/register.html' , context)

def loginUser(request):
     # e kshyrmi se nqoftse a asht useri logged in, nqoftse po at'her e qojm te profiles , nqoftse jo vazhdojm
    if request.user.is_authenticated:
        return redirect('home')

    #  nqoftse metoda osht POST <HTML>
    if request.method == "POST":
        # i mormi emrin e inputeve nhtml dhe ja i lidhmi me variablat
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            # e kshyrmi se a osht usernemi ndatabaz
            user = User.objects.get(username=username)
        except:
            pass
            # nqoftse jo at'her e qojm ni message 
            """
            messages i regjistrojm tek main.html
            """
            #messages.error(request , "Username does not exist")
        # nqoftese kejt jon nrregull at'her e bojm llog in 
        user = authenticate(request, username=username , password=password)
        # nqofte useri ndatabaz nuk osht i shprast , at'her e bojm llogin edhe e qojm tek profiles
        if user is not None:
            login(request , user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'editProfile') # account
        else:
            pass
        # nqoftse jo at'her e qesmi ket messazhin
            #messages.error(request , "Username or password is incorrect")

    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login') # login