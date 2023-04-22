from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from base.models import ielts, contact, course
from Everest.settings import MEDIA_ROOT, MEDIA_URL


# Create your views here.

def Home(request):
    context = {'ielts': ielts.objects.order_by("-id")}
    return render(request, 'base_templates/home.html', context)


def login(request):
    pass


