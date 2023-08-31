from django.urls import path

from audio_to_text.accounts.views import UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='profile_register'),
    path('login/', UserLoginView.as_view(), name='profile_login'),
    path('logout/', UserLogoutView.as_view(), name='profile_logout'),

)