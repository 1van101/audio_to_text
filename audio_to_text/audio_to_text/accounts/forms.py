from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from audio_to_text.accounts.models import UserProfile

UserModel = get_user_model()


class UserRegisterForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        widgets = {
            'password': forms.PasswordInput()
        }



    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = UserProfile(
            user=user,
        )
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        if commit:
            profile.save()
        return user


class LoginForm(auth_forms.AuthenticationForm):
    error_messages = {
        'invalid_login': 'Please enter a correct email and password!',
    }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'profile_picture']

        labels = {
            'username': 'Username',
            'profile_picture': 'Profile Picture'
        }