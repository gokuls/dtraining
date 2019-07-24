from django import forms

class LoginForm(forms.Form):
        username = forms.CharField(
                widget=forms.TextInput(attrs={'class':'form-control'}),
                help_text='Enter User Name')
        password = forms.CharField(
                label='Password',
                widget=forms.PasswordInput(
                    attrs={'class':'form-control','autocomplete':'off'}),
                help_text='Enter Password')
