from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Desktop,Laptop,Mobile)
class ViewAdmin(admin.ModelAdmin):
    pass