from django import forms

from base.models import location


class locationForm(forms.ModelForm):
    class Meta:
        model = location
        fields = ("address", "image", "instagram", "telegram", "phone_number1", "phone_number2")


class edit_locationForm(forms.ModelForm):
    class Meta:
        model = location
        fields = ("address", "image", "instagram", "telegram", "phone_number1", "phone_number2")
