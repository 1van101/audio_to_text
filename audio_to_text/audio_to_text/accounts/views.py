from django.contrib.auth import get_user_model, login
from django.contrib import messages
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from audio_to_text.accounts.forms import UserRegisterForm, LoginForm, UserEditForm
from audio_to_text.accounts.models import UserProfile

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


class UserDetailsView(views.DetailView):
    template_name = 'accounts/user-details-page.html'
    model = UserModel


class UserEditView(views.UpdateView):
    template_name = 'accounts/user-edit-page.html'

    model = UserProfile
    form_class = UserEditForm

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class UserDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/user-delete-page.html'
    success_url = reverse_lazy('index')


def signup_redirect(request):
    messages.error(
        request, "Something wrong here, it may be that you already have account!")
    return redirect('profile_login')
