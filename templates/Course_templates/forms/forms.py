from django import forms

from base.models import course


class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = ("level", "daytime", "subject", "teacher", "image")


class editCourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = ("level", "daytime", "subject", "teacher", "image")
