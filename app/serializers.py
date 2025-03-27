from rest_framework import serializers
from .models import *

class DoctorListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing doctors with minimal information (ID and name only).
    """
    class Meta:
        model=Doctor
        fields=['id','name']

class DoctorDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving detailed doctor information including specialization.
    """
    class Meta:
        model=Doctor
        fields=['id','name', 'specialization']

class PatientListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing patients with minimal information (ID and name only).
    """
    class Meta:
        model=Patient
        fields=['id','name']

class PatientDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving detailed patient information including age and medical history.
    """
    class Meta:
        model=Patient
        fields=['id','name', 'age', 'medical_history']


class PatientDoctorMappingCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a mapping between a patient and a doctor.
    Uses only IDs for patient and doctor.
    """
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_at']


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving patient-doctor mappings.
    Displays patient and doctor names instead of just IDs.
    """
    patient_name = serializers.CharField(source="patient.name", read_only=True)
    doctor_name = serializers.CharField(source="doctor.name", read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'assigned_at']

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Ensures password write-only for security.
    """
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            "username": {"required": True},  
            "email": {"required": True}
        }

    def create(self, validated_data):
        """
        Creates and returns a new user with an encrypted password.
        """
        return User.objects.create_user(**validated_data)