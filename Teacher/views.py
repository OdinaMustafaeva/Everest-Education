from django.shortcuts import render
from base.models import teacher


# Create your views here.

def Teacher(request):
    context = {'teacher': teacher.objects.order_by("-id")}
    return render(request, 'teacher_templates/main.html', context)


def Teacher_detail(request, pk):
    context = {'teacher': teacher.objects.order_by("-id")}
    return render(request, 'teacher_templates/main.html', context)
