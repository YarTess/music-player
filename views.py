from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from musicservice.forms import UserLoginForm, RegistrationForm

# @csrf_exempt
# def login_request(request):
#    if request.method == "POST":
#       form = UserLoginForm(request.POST)
#       if form.is_valid():
#          user = authenticate(
#                 username=form.cleaned_data["username"],
#                 password=form.cleaned_data["password"])
#          user = authenticate(request, username=username, password=password)
#
#                 login(request, user)
#                 return redirect('index')
#       else:
#           print(form.errors)
#       return render(request, 'login.html', {'form':form})

class IndexView(TemplateView):
    template_name = "main.html"

def login_request(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    context = {
        'form': form,
        'title': title,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        login(request, user)
        # messages.info(request, f"You are now logged in  as {user}")
        return redirect('index')
    else:
        print(form.errors)
        # messages.error(request, 'Username or Password is Incorrect! ')
    return render(request, 'login.html', context=context)


def signup_request(request):
    title = "Create Account"
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form': form, 'title': title}
    return render(request, 'signup.html', context=context)


def logout_request(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect('main')