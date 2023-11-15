from django.db import models

class UploadedZip(models.Model):
    zip_file = models.FileField(upload_to='uploaded_zips/')
    filename = models.CharField(max_length=255)
    rules = models.CharField(max_length=255)
    vul = models.CharField(max_length=255)
    def __str__(self):
        return self.filename