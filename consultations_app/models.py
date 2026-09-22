from django.db import models
from appointments_app.models import Booking
from accounts.models import Doctor, User

class Consultation(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='consultation')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consultation for Booking {self.booking.id}"

class Prescription(models.Model):
    consultation = models.OneToOneField(Consultation, on_delete=models.CASCADE, related_name='prescription')
    medications = models.TextField(help_text="List of medications and dosages")
    instructions = models.TextField(blank=True, null=True)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for Consultation {self.consultation.id}"
