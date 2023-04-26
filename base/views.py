from pyexpat.errors import messages
from base.models import ielts, Profile
from Everest.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.

def Home(request):
    context = {'ielts': ielts.objects.order_by("-id")}
    return render(request, 'base_templates/home.html', context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("base:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="base_templates/login.html", context={"login_form": form})


def register_page(request):
    if request.method == "POST":
        form = UserCreationForm(request)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("base:login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserCreationForm
    return render(request=request, template_name="base_templates/regitser.html",
                  context={"register_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("base:home")


def profile_page(request):
    try:
        profile = Profile.objects.get()
    except Exception:
        pass
    else:
        context = {"profile": profile}
        return render(request, 'base_templates/profile.html', context)
    return render(request, 'base_templates/profile.html')


def profile_edit(request):
    pass


def chat_page(request):
    return render(request, 'base_templates/chat.html')
