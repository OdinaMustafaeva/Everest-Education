from django.shortcuts import render


# Create your views here.

def Teacher(request):
    return render(request, 'teacher_templates/main.html')
