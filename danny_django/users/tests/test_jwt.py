import pytest
from django.urls import reverse
from rest_framework import status

from danny_django.users.models import User

pytestmark = pytest.mark.django_db


def test_jwt_token_obtain(client, user: User):
    url = reverse("token_obtain_pair")
    response = client.post(
        url,
        data={"username": user.username, "password": "password"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


def test_jwt_token_refresh(client, user: User):
    url = reverse("token_obtain_pair")
    response = client.post(
        url,
        data={"username": user.username, "password": "password"},
    )
    refresh_token = response.data["refresh"]

    url = reverse("token_refresh")
    response = client.post(url, data={"refresh": refresh_token})
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
