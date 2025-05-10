from django.urls import path
from .views import create_contact
from .views import health_check

urlpatterns = [
    path('create_contact/', create_contact),
]

urlpatterns = [
    path("healthz", health_check),
]