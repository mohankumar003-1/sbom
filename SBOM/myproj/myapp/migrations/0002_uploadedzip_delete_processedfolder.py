# Generated by Django 4.2.7 on 2023-11-15 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedZip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_file', models.FileField(upload_to='uploaded_zips/')),
            ],
        ),
        migrations.DeleteModel(
            name='ProcessedFolder',
        ),
    ]
