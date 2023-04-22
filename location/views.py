from django.shortcuts import render


# Create your views here.

def locations(request):
    return render(request, 'location_templates/main.html')


def location_detail(request, pk):
    pass
