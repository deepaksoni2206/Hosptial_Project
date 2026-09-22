from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import uuid
from .models import PaymentTransaction
from .serializers import PaymentTransactionSerializer
from appointments_app.models import Booking

class ProcessPaymentView(generics.CreateAPIView):
    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        booking_id = request.data.get('booking')
        if not booking_id:
            return Response({"detail": "booking is required."}, status=status.HTTP_400_BAD_REQUEST)
            
        booking = get_object_or_404(Booking, id=booking_id)
        
        # Verify the patient matches the logged-in user
        if booking.patient != request.user:
            return Response({"detail": "Not authorized to pay for this booking."}, status=status.HTTP_403_FORBIDDEN)
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # DUMMY PAYMENT PROCESSING
        # We just generate a fake transaction ID and set status to SUCCESS
        transaction_id = f"dummy_txn_{uuid.uuid4().hex[:10]}"
        
        serializer.save(
            status='SUCCESS',
            transaction_id=transaction_id
        )
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
