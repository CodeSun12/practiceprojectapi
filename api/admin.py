from django.contrib import admin
from .models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'f_name',
        'l_name',
        'email',
        'phone_no',
        'dob',
        'password',
        'cnic',
        'role',
        'gender',
        'image',
    ]