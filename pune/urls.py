from django.urls import path

from . import views

urlpatterns = [
    path('kerko-pune/', views.kerkoPune , name='kerko-pune'),
    path('shpall-pune/', views.shpallPune , name='shpall-pune'),
    path('view/<str:pk>/', views.singlePune , name='single-pune'),
]