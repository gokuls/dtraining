from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse



from .forms import LoginForm
from .forms import UserDetailsForm

from .models import UserDetails
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
               return render(request, 'fapp/login2.html', {'form': form,'error':True})
    else:
      form = LoginForm()
    return render(request, 'fapp/login2.html', {'form': form})


@login_required(login_url='')
def userCreation(request):
    print("in adding user")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print("User Creation")
        form = UserDetailsForm(request.POST)
        #print form
        # check whether it's valid:
        if form.is_valid():
           form.clean()
           obj = form.save()

           # process the data in form.cleaned_data as required
           # ..
           # redirect to a new URL:
           url = reverse('users')
           messages.info(request, 'User Added successfully')
           return HttpResponseRedirect(url)
        return render(request, 'fapp/useradd.html', {'form': form,'title':"User Registration"})

    else:
      form = UserDetailsForm()
      return render(request, 'fapp/useradd.html', {'form': form,'title':'User Registration'})

def userdetails(request):
    ud = UserDetails.objects.all()
    context_dict = { 'users' : ud }
    return render(request, 'fapp/userdetails.html', context=context_dict)


def returnUserDetail(request):
    if request.method == 'GET':
        username = request.GET['username']

        userdetails = list(UserDetails.objects.filter(username=username).values())
        strs = "<ul>"
        for i,j in userdetails[0].items():
            strs += "<li> %s : %s </li>"%(i,j)
        strs += "</ul>"
        #return JsonResponse(userdetails,safe=False)
        return HttpResponse(strs)
