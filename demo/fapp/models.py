from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(
                            max_length=24,
                            primary_key=True,
                            validators=[
        RegexValidator(
            regex='^[a-z][-a-z0-9_]*$',
            message='Username must be lower case character',
            code='invalid_username'
        ),
    ]
    )
    fullname            =   models.CharField(max_length=50, help_text='Full name of the user')
    rank                =   models.CharField(max_length=50)
    contact             =   models.CharField(max_length=50,help_text='contact number of user')
    email               =   models.EmailField(max_length=50)
    creation_date       =   models.DateTimeField(auto_now_add=True)
    userid              =   models.CharField(max_length=50,null=True,blank=True)
    userstatus          =   models.CharField(max_length=50,default='NOT MAPPED')

    def clean_username(self):
        data = self.cleaned_data['username']
        return data

    def __str__(self):
        return self.username

    @property
    def title(self):
        return self.username

