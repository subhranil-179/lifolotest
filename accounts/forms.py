from django.contrib.auth.forms import (UserCreationForm as AbstractUserCreationForm,
                                       UserChangeForm as AbstractUserChangeForm,)
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UserCreationForm(AbstractUserCreationForm):
    class Meta(AbstractUserCreationForm.Meta):
        model = User
        fields = AbstractUserCreationForm.Meta.fields


class UserChangeForm(AbstractUserChangeForm):
    class Meta(AbstractUserChangeForm.Meta):
        model = User
        fields = AbstractUserChangeForm.Meta.fields


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'username'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'username'}
        )
