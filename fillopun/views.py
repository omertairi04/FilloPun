from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from users.models import Profile , Skills
from pune.models import Pune

@login_required(login_url='login')
def Home(request):
    user = request.user.profile
    skill = request.user.profile.skills.all()
    pune = Pune.objects.distinct().filter(skills__in=skill).exclude(business__exact=user)

    context = {
        'skill':skill,
        'pune':pune
    }

    return render(request , 'home.html', context)
