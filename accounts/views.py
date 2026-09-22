from rest_framework import generics, permissions
from .models import User, Profile, Doctor
from .serializers import UserSerializer, ProfileSerializer, DoctorSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.filter(is_verified=True)
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]
