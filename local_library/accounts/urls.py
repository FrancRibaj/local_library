from django.urls import path, include
from . import views

#Add Django site authentication urls (for login, logout, password management)

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name= 'signup')
]
