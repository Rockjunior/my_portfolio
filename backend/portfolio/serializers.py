# Import the serializers module from the Django REST framework
from rest_framework import serializers
# Import the AcademicExperience and SWEExperience models from the local models file
from .models import AcademicExperience, SWEExperience

# Define a serializer for the AcademicExperience model
class AcademicExperienceSerializer(serializers.ModelSerializer):
    class Meta:  # Meta class to specify configuration options for the serializer 
    # Specify which model the serializer is associated with
        model = AcademicExperience
        fields = '__all__'

class SWEExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SWEExperience
        fields = '__all__'
