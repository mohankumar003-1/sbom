from django.urls import path
from .views import upload_zip,download_text_file

urlpatterns = [
    path('upload/', upload_zip, name='upload_zip'),
    path('download/<path:file_path>/', download_text_file, name='download_text_file'),

]
