from django.contrib.auth import get_user_model, login

from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from audio_to_text.accounts.forms import UserRegisterForm, LoginForm

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    model = UserModel
    form_class = UserRegisterForm
    template_name = 'accounts/user-register-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/user-login-page.html'
    form_class = LoginForm


class UserLogoutView(auth_views.LogoutView):
    pass
