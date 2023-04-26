from django.shortcuts import render
from base.models import location, contact, teacher


# Create your views here.

def locations(request):
    location_ = contact.objects.order_by("-id")
    context = {'location': location_}
    return render(request, 'location_templates/main.html', context)


def location_detail(request, pk):
    try:
        count_work = teacher.objects.filter(work_id=pk).count()
        location_ = contact.objects.filter(address_id=pk)[0]
    except Exception:
        return render(request, 'location_templates/location_detail.html')
    else:
        context = {'location': location_, 'count_people': count_work}
        return render(request, 'location_templates/location_detail.html', context)
