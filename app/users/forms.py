from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SystemUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = SystemUser
        fields = ('first_name', 'last_name', 'email', 'phone',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = SystemUser
        fields = ('email',)
