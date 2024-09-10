from rest_framework import serializers
from .models import AcademicExperience, SWEExperience

class AcademicExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicExperience
        fields = '__all__'

class SWEExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SWEExperience
        fields = '__all__'