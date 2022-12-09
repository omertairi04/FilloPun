from django.shortcuts import render

from users.models import Profile , Skills
from pune.models import Pune

def Home(request):
    skill = request.user.profile.skills.all()
    pune = Pune.objects.distinct().filter(skills__in=skill)

    context = {
        'skill':skill,
        'pune':pune
    }

    return render(request , 'home.html', context)
