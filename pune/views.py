from django.shortcuts import render

def kerkoPune(request):

    context = {}
    return render(request , 'pune/kerkopune.html',context)
