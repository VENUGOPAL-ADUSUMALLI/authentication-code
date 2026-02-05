from django.urls import path
from authentication.views import signup_view, signin_view, profile_view

app_name = 'authentication'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('profile/', profile_view, name='profile'),
]
