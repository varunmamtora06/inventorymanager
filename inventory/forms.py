from django.forms import ModelForm
from .models import *

class LaptopForm(ModelForm):
    class Meta:
        model = Laptop
        fields ='__all__'

class DesktopForm(ModelForm):
    class Meta:
        model = Desktop
        fields ='__all__'

class MobileForm(ModelForm):
    class Meta:
        model = Mobile
        fields ='__all__'
