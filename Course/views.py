from django.shortcuts import render


# Create your views here.

def Course(request):
    return render(request, 'Course_templates/main.html')
