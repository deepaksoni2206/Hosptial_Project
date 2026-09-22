import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User, Profile

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_user_registration(api_client):
    url = reverse('register')
    data = {
        'username': 'testpatient',
        'email': 'patient@test.com',
        'password': 'password123',
        'role': 'PATIENT'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    
    # Verify user and profile were created
    user = User.objects.get(username='testpatient')
    assert user.role == 'PATIENT'
    assert Profile.objects.filter(user=user).exists()

@pytest.mark.django_db
def test_login(api_client):
    user = User.objects.create_user(username='testuser', password='password123', role='PATIENT')
    url = reverse('token_obtain_pair')
    data = {
        'username': 'testuser',
        'password': 'password123'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data
