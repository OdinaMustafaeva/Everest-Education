from django.db.models import Q
from django.shortcuts import render, redirect
from templates.Course_templates.forms.forms import CourseForm, editCourseForm
from base.models import course, students, teacher


# Create your views here.

def Course(request):
    course_ = course.objects.order_by("-id")
    context = {'course1': course_}
    return render(request, 'Course_templates/main.html', context)


def Course_detail(request, pk):
    try:
        student = students.objects.filter(course_id=pk).count()
        course_ = course.objects.filter(id=pk)[0]
    except Exception:
        return render(request, 'Course_templates/main.html')
    else:
        context = {'course': course_, 'student': student}
        return render(request, 'Course_templates/course-details.html', context)


def course_search(request):
    search_query = request.POST.get("search_course")
    expression = course.objects.filter(subject__name=search_query)
    return render(request, "Course_templates/course_search.html", {"results": expression})


def new_add(request):
    if request.POST:
        form = editCourseForm(request.POST)
        form.save()
        return redirect("course:Course_main")
    else:
        form = editCourseForm()
    context = {'form': form}
    return render(request, 'Course_templates/course_add.html', context)


def course_edit(request, p_k):
    course_ = course.objects.get(id=p_k)
    if request.POST:
        form = editCourseForm(request.POST)
        form.save(course_)
        return redirect("course:Course_main")
    else:
        form = editCourseForm()
    context = {'form': form}
    return render(request, 'Course_templates/course_update.html', context)


def course_delete(request, pk):
    cous_e = course.objects.get(id=pk)
    if request.method == 'POST':
        cous_e.delete()
        return redirect('course:Course_main')
    return render(request, 'delete.html', {'obj': cous_e})
