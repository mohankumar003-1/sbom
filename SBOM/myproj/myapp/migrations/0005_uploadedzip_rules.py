# Generated by Django 4.2.5 on 2023-11-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_uploadedzip_rules_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedzip',
            name='rules',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
