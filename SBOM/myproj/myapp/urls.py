from django.urls import path
from .views import upload_zip

urlpatterns = [
    path('upload/', upload_zip, name='upload_zip'),
]
