# Generated by Django 5.0.6 on 2024-06-01 21:19

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("between_app", "0013_alter_ps_group_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ps_group",
            name="image",
            field=models.ImageField(
                height_field="300",
                storage=django.core.files.storage.FileSystemStorage(
                    base_url="/uploads", location="static/"
                ),
                upload_to="",
                width_field="200",
            ),
        ),
    ]