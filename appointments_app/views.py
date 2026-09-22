from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db import transaction
from .models import AvailabilitySlot, Booking
from .serializers import AvailabilitySlotSerializer, BookingSerializer

class AvailabilitySlotListView(generics.ListCreateAPIView):
    queryset = AvailabilitySlot.objects.all()
    serializer_class = AvailabilitySlotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Only doctors can create slots for themselves
        if hasattr(self.request.user, 'doctor_profile'):
            serializer.save(doctor=self.request.user.doctor_profile)

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        slot_id = serializer.validated_data['slot'].id
        
        with transaction.atomic():
            # Lock the slot row to prevent concurrent bookings
            slot = AvailabilitySlot.objects.select_for_update().get(id=slot_id)
            if slot.is_booked:
                return Response({'detail': 'Slot already booked'}, status=status.HTTP_400_BAD_REQUEST)
            
            slot.is_booked = True
            slot.save()
            
            booking = serializer.save(patient=request.user)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
