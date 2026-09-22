from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Consultation, Prescription
from .serializers import ConsultationSerializer, PrescriptionSerializer
from appointments_app.models import Booking

class ConsultationCreateView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        booking_id = request.data.get('booking_id')
        if not booking_id:
            return Response({"detail": "booking_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        booking = get_object_or_404(Booking, id=booking_id)
        
        # Verify the doctor matches the logged-in doctor
        if not hasattr(request.user, 'doctor_profile') or booking.slot.doctor != request.user.doctor_profile:
            return Response({"detail": "Not authorized to create consultation for this booking."}, status=status.HTTP_403_FORBIDDEN)
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(booking=booking)
        
        # Mark booking as completed
        booking.status = 'COMPLETED'
        booking.save()
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PrescriptionCreateView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        consultation_id = request.data.get('consultation_id')
        if not consultation_id:
            return Response({"detail": "consultation_id is required."}, status=status.HTTP_400_BAD_REQUEST)
            
        consultation = get_object_or_404(Consultation, id=consultation_id)
        
        # Verify doctor
        if not hasattr(request.user, 'doctor_profile') or consultation.booking.slot.doctor != request.user.doctor_profile:
            return Response({"detail": "Not authorized."}, status=status.HTTP_403_FORBIDDEN)
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(consultation=consultation)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
