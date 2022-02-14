from rest_framework import serializers
from .models import Student, Tutor
class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['sid', 'sname', 'semail', 'spassword']

class TutorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tutor
    fields = ['tid', 'tname', 'temail', 'tpassword']    