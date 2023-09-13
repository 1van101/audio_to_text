from django.contrib.auth import models as auth_models, get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from audio_to_text.accounts.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True
    )
    date_joined = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()


UserModel = get_user_model()


class UserProfile(models.Model):
    USERNAME_MAX_LEN = 30
    USERNAME_MIN_LEN = 2

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE
    )

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(limit_value=USERNAME_MIN_LEN,
                                       message='Ensure username has at least 2 characters (it has 1).')]
    )


    profile_picture = models.ImageField(
        upload_to='profile_img/',
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.user.email
        super().save(*args, **kwargs)
