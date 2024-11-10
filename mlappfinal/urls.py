from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict, name='predict'),  # Ensure this matches exactly
]
