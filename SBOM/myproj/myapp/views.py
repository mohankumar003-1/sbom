# views.py
from django.shortcuts import render, redirect
from .forms import ZipUploadForm
from .models import UploadedZip
import os
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .code import folderaccess
import zipfile
from django.utils import timezone
import shutil
def handle_uploaded_zip(zip_file):
    extract_path = 'media/extracted_zips/'
    
    # Create or clear the extraction directory
    if os.path.exists(extract_path):
        shutil.rmtree(extract_path)
    
    os.makedirs(extract_path, exist_ok=True)
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    
    # Continue with the rest of your code
    directories = [d for d in os.listdir(extract_path) if os.path.isdir(os.path.join(extract_path, d))]
    for directory in directories:
        a = directory
        
    return folderaccess()
def upload_zip(request):
    if request.method == 'POST':
        form = ZipUploadForm(request.POST, request.FILES)
        if form.is_valid():
            zip_file = form.save()
            print(zip_file)
            soln_list = handle_uploaded_zip(zip_file.zip_file.path)
            uploaded_file = form.save(commit=False)
            uploaded_file.filename = request.FILES['zip_file'].name
            uploaded_file.rules = soln_list[1]
            if soln_list[0] == 2 :
                uploaded_file.vul = 'HIGH'
            elif soln_list[0] == 1 :
                uploaded_file.vul = 'MEDIUM'
            else:
                uploaded_file.vul = 'LOW'
            print(uploaded_file.vul)
            uploaded_file.save()
            # latest_object = UploadedZip.objects.order_by('-id').first()

            # if latest_object:
            #     # Delete objects with id less than the maximum id
            #     old_objects = UploadedZip.objects.filter(id__lt=latest_object.id)
            #     old_objects.delete()
    
            return redirect('upload_zip')
    else:
        form = ZipUploadForm()
    files = UploadedZip.objects.all()
    return render(request, 'upload_zip.html', {'form': form, 'files': files})


def download_text_file(request, file_path):
    file_path = os.path.join(r'C:\Users\MOHANKUMAR\PROJECTS\Machine Learning\sbom\SBOM\myproj\media\extracted_zips\test', file_path)
    
    if not os.path.exists(file_path) or not file_path.endswith('.txt'):
        return HttpResponse("File not found or invalid file type.", status=404)
    
    file_name = os.path.basename(file_path)
    
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
    return response
