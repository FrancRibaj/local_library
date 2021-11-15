from django.urls import path, include

#Add Django site authentication urls (for login, logout, password management)

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
