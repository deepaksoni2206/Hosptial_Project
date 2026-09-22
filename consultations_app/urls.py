from django.urls import path
from .views import ConsultationCreateView, PrescriptionCreateView

urlpatterns = [
    path('consultations/', ConsultationCreateView.as_view(), name='consultation-create'),
    path('prescriptions/', PrescriptionCreateView.as_view(), name='prescription-create'),
]
