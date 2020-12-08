from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def save(self):
        user = super(UserCreationForm, self).save(commit=True)  # if remove raise error
        # as email not in super
        user.email = self.cleaned_data.get('email')
        print(self.Meta.help_texts)
        user.save()
        return user

    class Meta:
        model = User
        fields = (
                'username',
                'email',
                'password1',
                'password2',
        )
        help_texts = {
                'username':  None,
                'email':     None,
                'password1': None,
                'password2': None,
        }

    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user


class CustomCreateUserForm(forms.Form):
    username = forms.CharField(label='Enter username',
                               required=True,
                               min_length=4,
                               max_length=15)
    email = forms.EmailField(label='Enter email',
                             help_text='Custom help text')
    password = forms.CharField(label='password',
                                      widget=forms.PasswordInput)
    passwordConfirm = forms.CharField(label='confirm password',
                                      widget=forms.PasswordInput)
    firstname = forms.CharField(label='Enter your name')
    lastname = forms.CharField(label='Enter your surname')

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password(self):
        confirm = self.cleaned_data.get('passwordConfirm')
        pswd = self.cleaned_data.get('password')

        if confirm and pswd and confirm != pswd:
            raise ValidationError("passwords do not match")

        return pswd

    def save(self):
        user = User.objects.create_user(
                self.cleaned_data.get('username'),
                self.cleaned_data.get('email'),
                self.cleaned_data.get('password'),
                first_name=self.cleaned_data.get('firstname'),
                last_name=self.cleaned_data.get('lastname'),
                is_staff=True,
        )
        return user
