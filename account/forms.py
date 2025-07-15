from django import  forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from account.models import Profile


class Loginform(forms.Form):
    username = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'input100','placeholder':'Username'}))
    password = forms.CharField(max_length=50
                               , widget=forms.PasswordInput(attrs={'class':'input100' , 'placeholder':'Password'}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data['username'],password=self.cleaned_data['password'])
        if user is not None:
            return self.cleaned_data['password']

        raise ValidationError('Username or password is incorrect')


class Profileform(forms.ModelForm):
    class Meta:
            model = Profile
            fields = '__all__'
