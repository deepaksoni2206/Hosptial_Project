from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('PATIENT', 'Patient'),
        ('DOCTOR', 'Doctor'),
        ('ADMIN', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='PATIENT')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.CharField(max_length=100)
    experience_years = models.IntegerField(default=0)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} - {self.specialty}"

