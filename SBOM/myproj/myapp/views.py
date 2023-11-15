# views.py
from django.shortcuts import render, redirect
from .forms import ZipUploadForm
from .models import UploadedZip
import os
from .code import folderaccess
import zipfile

def handle_uploaded_zip(zip_file):
    extract_path = 'media/extracted_zips/'
    os.makedirs(extract_path, exist_ok=True)
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    directories = [d for d in os.listdir(extract_path) if os.path.isdir(os.path.join(extract_path, d))]
    for directory in directories:
        a = directory
        print(a)
    return folderaccess()
def upload_zip(request):
    if request.method == 'POST':
        form = ZipUploadForm(request.POST, request.FILES)
        if form.is_valid():
            zip_file = form.save()
            soln_list = handle_uploaded_zip(zip_file.zip_file.path)
            uploaded_file = form.save(commit=False)
            uploaded_file.filename = request.FILES['zip_file'].name
            uploaded_file.rules = soln_list[1]
            if soln_list[0] == 2 :
                uploaded_file.vul = 'HIGH'
            elif soln_list[0] == 1 :
                uploaded_file.vul = 'MEDIUM'
            else:
                uploaded_file.vulnerability = 'LOW'
            print(uploaded_file.vul)
            uploaded_file.save()
            return redirect('upload_zip')
    else:
        form = ZipUploadForm()
    files = UploadedZip.objects.all()
    return render(request, 'upload_zip.html', {'form': form, 'files': files})

