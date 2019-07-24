from django import forms
from .models import UserDetails

from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Textarea
from django.forms import DateTimeInput
from django.forms import HiddenInput
from django.forms import CheckboxInput
from django.forms import Select

from django.utils.translation import ugettext_lazy as _



class LoginForm(forms.Form):
        username = forms.CharField(
                widget=forms.TextInput(attrs={'class':'form-control'}),
                help_text='Enter User Name')
        password = forms.CharField(
                label='Password',
                widget=forms.PasswordInput(
                    attrs={'class':'form-control','autocomplete':'off'}),
                help_text='Enter Password')


class UserDetailsForm(ModelForm):
        class Meta:
            model = UserDetails
            def clean_name(self):
                data = self.cleaned_data['username']
                return data

            fields = (
                        'username','fullname','rank','contact',
                        'email','userid'
                    )

            labels = {
                    'username': _('User Name'),
                    'rank': _('Rank')
                  }
            widgets = {
                        'username' : TextInput(attrs={'class':'form-control'}),
                        'fullname' : TextInput(attrs={'class':'form-control'}),
                        'rank' : TextInput(attrs={'class':'form-control'}),
                        'contact' : TextInput(attrs={'class':'form-control'}),
                        'email' : TextInput(attrs={'class':'form-control'}),
                        'userid' : TextInput(attrs={'class':'form-control'}),
                  }
