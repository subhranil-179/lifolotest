from django.contrib.auth.forms import (UserCreationForm as AbstractUserCreationForm,
                                       UserChangeForm as AbstractUserChangeForm,)
from django.contrib.auth.forms import AuthenticationForm
from .models import User, UserProfile
from django import forms


class UserCreationForm(AbstractUserCreationForm):
    class Meta(AbstractUserCreationForm.Meta):
        model = User
        fields = AbstractUserCreationForm.Meta.fields


class UserChangeForm(AbstractUserChangeForm):
    class Meta(AbstractUserChangeForm.Meta):
        model = User
        fields = AbstractUserChangeForm.Meta.fields


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileUpdateForm(forms.ModelForm):
    # image = forms.ImageField(widget=forms.FileInput(attrs={"class": "hello"}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bio'].required = False

    class Meta:
        model = UserProfile
        fields = ['image', 'bio']
        widgets = {
                'bio': forms.Textarea(attrs={'name': 'bio', 'id': 'bio', 'placeholder': "Tell others something about yourself.", 'rows': "2"}),
        }
        labels = {
            'image': '',
        }


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'username'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'username'}
        )
