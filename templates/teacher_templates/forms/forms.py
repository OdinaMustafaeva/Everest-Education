from django import forms

from base.models import teacher


class teacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ("phone_number", "age", "victories", "image", "name", "work")


class editteacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ("phone_number", "age", "victories", "image", "name", "work")
