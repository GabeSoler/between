# Generated by Django 5.1.1 on 2024-10-11 12:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("learning_logs", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shadow",
            name="owner",
        ),
        migrations.DeleteModel(
            name="Creation",
        ),
        migrations.DeleteModel(
            name="Shadow",
        ),
    ]