"""
URL configuration for the healthcare project.

This file maps API endpoints to their respective views. It includes authentication,
patient and doctor management, patient-doctor mapping APIs and logout.
"""

from django.urls import path
from app.views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Authentication Endpoints
    path('api/auth/register/', RegisterView.as_view(), name='register'),  # User registration
    path('api/auth/login/', LoginView.as_view(), name='login'),  # User login (returns JWT)
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT access token
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),  # Logout and blacklist refresh token

    # Patient Management Endpoints
    path('api/patients/', PatientListCreateView.as_view(), name='patient-list-create'),  # List & create patients
    path('api/patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),  # Retrieve, update, delete patient

    # Doctor Management Endpoints
    path('api/doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),  # List & create doctors
    path('api/doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),  # Retrieve, update, delete doctor

    # Patient-Doctor Mapping Endpoints
    path('api/mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),  # Assign doctor to patient
    path('api/mappings/<int:patient_id>/', PatientDoctorMappingByPatientView.as_view(), name='mapping-by-patient'),  # Get doctors assigned to a patient
    path('api/mappings/delete/<int:pk>/', PatientDoctorMappingDeleteView.as_view(), name='mapping-delete'),  # Remove doctor from patient
]
