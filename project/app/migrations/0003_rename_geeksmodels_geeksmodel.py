# Generated by Django 3.2.5 on 2023-01-17 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_greeksmodels_geeksmodels'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeeksModels',
            new_name='GeeksModel',
        ),
    ]
