from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    """
    Model representing a patient.

    Attributes:
        user (ForeignKey): Links the patient to a specific user.
        name (CharField): Stores the patient's name.
        age (IntegerField): Stores the patient's age.
        medical_history (TextField): Stores the patient's medical history.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    medical_history = models.TextField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    """
    Model representing a doctor.

    Attributes:
        user (ForeignKey): Links the doctor to a specific user.
        name (CharField): Stores the doctor's name (unique).
        specialization (CharField): Doctor's area of expertise.
        created_at (DateTimeField): Timestamp of when the doctor was created.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    specialization = models.CharField(max_length=150)

    def __str__(self):
        return f'Dr. self.name'

class PatientDoctorMapping(models.Model):
    """
    Model representing the mapping between a patient and a doctor.

    Attributes:
        patient (ForeignKey): References the patient.
        doctor (ForeignKey): References the doctor.
        assigned_at (DateTimeField): Timestamp of when the doctor was assigned to the patient.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')  # Prevent duplicate mappings

    def __str__(self):
        return f"{self.patient.name} assigned to Dr. {self.doctor.name} on {self.assigned_at}"
