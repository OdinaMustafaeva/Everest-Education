from django.forms import ModelForm
from models import location


class location_form(ModelForm):
    class Meta:
        model = location
        fields = '__all__'
