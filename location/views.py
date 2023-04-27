from django.shortcuts import render, redirect
from base.models import location, teacher
from templates.location_templates.forms.forms import edit_locationForm, locationForm


# Create your views here.

def locations(request):
    location_ = location.objects.order_by("-id")
    context = {'location': location_}
    return render(request, 'location_templates/main.html', context)


def location_detail(request, pk):
    try:
        count_work = teacher.objects.filter(work_id=pk).count()
        location_ = location.objects.get(id=pk)
    except Exception:
        return render(request, 'location_templates/location_detail.html')
    else:
        context = {'location': location_, 'count_people': count_work}
        return render(request, 'location_templates/location_detail.html', context)


def edit_location(request, p_k):
    location_ = location.objects.get(id=p_k)
    if request.POST:
        form = edit_locationForm(request.POST)
        form.save(location_)
        return redirect("teacher:teacher_")
    else:
        form = edit_locationForm()
    context = {'form': form}
    return render(request, 'location_templates/edit_location.html', context)


def delete_location(request, pk):
    location_1 = location.objects.get(id=pk)
    if request.method == 'POST':
        location_1.delete()
        return redirect('location:location_')
    return render(request, 'delete.html', {'obj': location_1})


def new_add(request):
    if request.POST:
        form = locationForm(request.POST)
        form.save()
        return redirect("location:location_")
    else:
        form = locationForm()
    context = {'form': form}
    return render(request, 'location_templates/add_new.html', context)
