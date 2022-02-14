from django.db import models

# Create your models here.
class Student(models.Model):
  sid = models.AutoField(primary_key=True)
  sname = models.CharField(max_length=30)
  semail = models.EmailField(max_length=30,unique = True)
  spassword = models.CharField(max_length=20)

class Tutor(models.Model):
  # student = models.ForeignKey(Student, on_delete=models.CASCADE)
  tid = models.AutoField(primary_key=True)
  tname = models.CharField(max_length=30)
  temail = models.EmailField(max_length=30,unique = True)
  tpassword = models.CharField(max_length=20)
