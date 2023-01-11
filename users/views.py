from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import UserRegisterForm , EditProfileForm , MessageForm
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
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile' , username = profile.username)
        
    context = {
        'profile':profile,
        'form':form
    }

    return render(request , 'users/edit-account.html', context)

def puntor(request):
    profiles = Profile.objects.all()

    context = {
        'profiles':profiles,
    }
    return render(request , 'users/puntor.html', context)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()

    context = {
        'messageRequests':messageRequests,
        'unreadCount':unreadCount,
    }

    return render(request , 'users/inbox.html', context)

@login_required(login_url='login')
def viewMessage(request , pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message':message}
    return render(request , 'users/message.html', context)

def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            # add sender to message
            message.sender = sender
            # add recipient to message
            message.recipient = recipient

            if sender:
                # when user is signedd in we send the name and email manually through this
                message.name = sender.name
                message.email = sender.email
            
            message.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('user-profile' , pk=recipient.id)

    context = {
        'recipient':recipient,
        'form':form
    }   
    return render(request , 'users/message_form.html',context)

def registerUser(request):
    page = 'user'
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request , 'Successfully registered')

            login(request , user)
            return redirect('home')
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
            return redirect(request.GET['next'] if 'next' in request.GET else 'home') # account
        else:
            pass
        # nqoftse jo at'her e qesmi ket messazhin
            #messages.error(request , "Username or password is incorrect")

    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login') # login