from django.contrib import admin
from .models import Student,Tutor
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['sid', 'sname','semail','spassword']

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
  list_display = ['tid', 'tname','temail','tpassword']
