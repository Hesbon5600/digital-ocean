from django.urls import path
from .views import (RegistrationAPIView,)


urlpatterns = [
    path('', RegistrationAPIView.as_view(), name='user-registration'),
]
