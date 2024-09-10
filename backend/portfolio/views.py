from rest_framework import viewsets
from .models import AcademicExperience, SWEExperience
from .serializers import AcademicExperienceSerializer, SWEExperienceSerializer

class AcademicExperienceViewSet(viewsets.ModelViewSet):
    queryset = AcademicExperience.objects.all()
    serializer_class = AcademicExperienceSerializer

class SWEExperienceViewSet(viewsets.ModelViewSet):
    queryset = SWEExperience.objects.all()
    serializer_class = SWEExperienceSerializer