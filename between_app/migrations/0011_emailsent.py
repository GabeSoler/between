# Generated by Django 4.2.13 on 2024-05-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("between_app", "0010_ps_section_ps_group"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailSent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
