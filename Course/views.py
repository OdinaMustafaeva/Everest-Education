from django.db.models import Q
from django.shortcuts import render

from base.models import course, students


# Create your views here.

def Course(request):
    course_ = course.objects.order_by("-id")
    context = {'course1': course_}
    return render(request, 'Course_templates/main.html', context)


def Course_detail(request, pk):
    student = students.objects.filter(course_id=pk).count()
    course_ = course.objects.get(id=pk)
    context = {'course': course_, 'student': student}
    return render(request, 'Course_templates/course-details.html', context)


def course_search(request):
    search_query = request.POST.get("search_course")
    expression = course.objects.all()
    return render(request, "Course_templates/course_search.html", {"results": expression})


def course_name(request, pk):
    context = course.objects.filter(subject=pk)
    return render(request, 'Course_templates/course_n.html', {'course_': context})
