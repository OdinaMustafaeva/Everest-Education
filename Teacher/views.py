from django.shortcuts import render, redirect
from base.models import teacher
from templates.teacher_templates.forms.forms import editteacherForm, teacherForm


# Create your views here.

def Teacher(request):
    context = {'teacher': teacher.objects.order_by("-id")}
    return render(request, 'teacher_templates/main.html', context)


def Teacher_detail(request, pk):
    try:
        teachers = teacher.objects.filter(id=pk)[0]
    except Exception:
        return render(request, 'teacher_templates/main.html')
    else:
        context = {'my_teacher': teachers}
        return render(request, 'teacher_templates/teacher_detail.html', context)


def new_add(request):
    if request.POST:
        form = editteacherForm(request.POST)
        form.save()
        return redirect("teacher:teacher_")
    else:
        form = editteacherForm()
    context = {'form': form}
    return render(request, 'teacher_templates/add_new.html', context)


def teacher_edit(request, p_k):
    teacher_ = teacher.objects.get(id=p_k)
    if request.POST:
        form = editteacherForm(request.POST)
        form.save(teacher_)
        return redirect("teacher:teacher_")
    else:
        form = editteacherForm()
    context = {'form': form}
    return render(request, 'Course_templates/course_update.html', context)


def teacher_delete(request, pk):
    teacher_3 = teacher.objects.get(id=pk)
    if request.method == 'POST':
        teacher_3.delete()
        return redirect('teacher:teacher_')
    return render(request, 'delete.html', {'obj': teacher_3})
