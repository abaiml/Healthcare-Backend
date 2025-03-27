from rest_framework import generics, permissions, status
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


# Authentication APIs

class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    Allows any user to register by providing a username, email, and password.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(TokenObtainPairView):
    """
    API endpoint for user login.
    Uses JWT for authentication.
    """
    permission_classes = [permissions.AllowAny]


# Patient Management APIs

class PatientListCreateView(generics.ListCreateAPIView):
    """
    API endpoint to create and list patients.
    - GET: Lists all patients for the authenticated user.
    - POST: Creates a new patient under the authenticated user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user) # Show only user’s patients
    
    def get_serializer_class(self): 
        if self.request.method=="GET":
            return PatientListSerializer  
        return PatientDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign current user


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, or delete a specific patient.
    - GET: Retrieve patient details.
    - PUT: Update patient details.
    - DELETE: Delete a patient.
    """
    serializer_class = PatientDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)


# Doctor Management APIs

class DoctorListCreateView(generics.ListCreateAPIView):
    """
    API endpoint to create and list doctors.
    - GET: Lists all doctors.
    - POST: Creates a new doctor.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.all()  # Return all doctors

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DoctorListSerializer  # Show only ID & Name
        return DoctorDetailSerializer  # Use full details for creating

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign current user


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, or delete a specific doctor.
    - GET: Retrieve doctor details.
    - PUT: Update doctor details.
    - DELETE: Delete a doctor.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


# Patient-Doctor Mapping APIs

class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    """
    API endpoint to list and assign doctors to patients.
    - GET: Retrieve all mappings.
    - POST: Assign a doctor to a patient.
    """
    queryset = PatientDoctorMapping.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PatientDoctorMappingCreateSerializer  # Use minimal fields
        return PatientDoctorMappingSerializer  # Use detailed view for GET


class PatientDoctorMappingByPatientView(generics.ListAPIView):
    """
    API endpoint to retrieve all doctors assigned to a specific patient.
    """
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)


class PatientDoctorMappingDeleteView(generics.DestroyAPIView):
    """
    API endpoint to remove a doctor from a patient.
    """
    queryset = PatientDoctorMapping.objects.all()
    permission_classes = [permissions.IsAuthenticated]

# Logout API

class LogoutView(APIView):
    """
    API endpoint to log out a user by blacklisting their refresh token.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the refresh token
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)