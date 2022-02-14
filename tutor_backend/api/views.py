from .models import Student, Tutor
from .serializers import StudentSerializer,TutorSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class TutorList(ListAPIView):
  queryset = Tutor.objects.all()
  serializer_class = TutorSerializer