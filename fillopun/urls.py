from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

from .views import Home
urlpatterns = [
    path('', Home , name='home'),
    path('admin/', admin.site.urls),

    path('', include('users.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
