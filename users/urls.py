from django.urls import path

from . import views

urlpatterns =  [
    path('register/user/',views.registerUser , name='register-user'),
#    path('register/bussiness/',views.register , name='register-bussiness'),
    path('logout/', views.logoutUser , name='logout'),
    path('login/', views.loginUser , name='login'),

    path('profile/<str:username>/', views.profile , name='profile'),
    path('edit-profile/', views.editProfile , name='edit-profile'),
    path('puntor/' , views.puntor , name="puntor"),

    path('inbox/', views.inbox , name='inbox'),
    path('message/<str:pk>/',views.viewMessage, name='message'),
    path('create-message/<str:pk>/',views.createMessage, name='create-message'),
]

