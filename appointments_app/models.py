from django.db import models
from accounts.models import Doctor, User

class AvailabilitySlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availability_slots')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('doctor', 'date', 'start_time')

    def __str__(self):
        return f"{self.doctor} - {self.date} {self.start_time} to {self.end_time}"

class Booking(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    )
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    slot = models.OneToOneField(AvailabilitySlot, on_delete=models.PROTECT, related_name='booking')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.id} for {self.patient.username} at {self.slot.date} {self.slot.start_time}"
