from django.urls import path

from . import views

urlpatterns = [
    path('kerko-pune/', views.kerkoPune , name='kerko-pune')
]