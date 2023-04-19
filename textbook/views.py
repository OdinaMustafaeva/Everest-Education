from django.shortcuts import render


# Create your views here.

def textbook(request):
    return render(request, 'textbook_templates/main.html')
