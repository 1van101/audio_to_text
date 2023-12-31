from django.urls import path, include

from audio_to_text.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, UserEditView, UserDetailsView, \
    UserDeleteView, signup_redirect

urlpatterns = (

    path('register/', UserRegisterView.as_view(), name='profile_register'),
    path('login/', UserLoginView.as_view(), name='profile_login'),
    path('login/google/login/', signup_redirect, name='signup_redirect'),
    path('logout/', UserLogoutView.as_view(), name='profile_logout'),
    path('<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='profile_details'),
        path('edit/', UserEditView.as_view(), name='profile_edit'),
        path('delete/', UserDeleteView.as_view(), name='profile_delete'),
    ])),

)
