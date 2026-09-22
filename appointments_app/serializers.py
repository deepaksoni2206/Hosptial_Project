from rest_framework import serializers
from .models import AvailabilitySlot, Booking
from accounts.serializers import DoctorSerializer

class AvailabilitySlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilitySlot
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('patient', 'status')
