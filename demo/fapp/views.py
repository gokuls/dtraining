from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect


from .forms import LoginForm
# Create your views here.

def index(request):
  return HttpResponse("This is first example")


def ulogin(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # print "IP accessing the machine----",request.META['REMOTE_ADDR']
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
           username =  form.cleaned_data['username']
           password = form.cleaned_data['password']

           # process the data in form.cleaned_data as required
           # ..
           # redirect to a new URL:
           user = authenticate(username=username, password=password)
           if user is not None:
               if user.is_active:
                   login(request, user)
                   url = reverse('index')
                   return HttpResponseRedirect(url)
               else:
                   context_dict = { 'status' : "incorrect credentials" }
                   return render(request,'fapp/failure.html',context=context_dict)
           else:
               context_dict = { 'status' : "Login failure" }
               form = LoginForm()
               return render(request, 'fapp/login.html', {'form': form,'error':True})
    else:
      form = LoginForm()
    return render(request, 'fapp/login.html', {'form': form})
