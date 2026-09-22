from django.urls import path
from .views import AvailabilitySlotListView, BookingCreateView

urlpatterns = [
    path('slots/', AvailabilitySlotListView.as_view(), name='availability-slot-list'),
    path('bookings/', BookingCreateView.as_view(), name='booking-create'),
]
