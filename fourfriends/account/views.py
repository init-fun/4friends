from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated Successfully")
                else:
                    return HttpResponse("Disabled accout")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "account/login.html", context)
