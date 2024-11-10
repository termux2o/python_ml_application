from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mlappfinal.urls')),  # Include URLs from mlappfinal
]
