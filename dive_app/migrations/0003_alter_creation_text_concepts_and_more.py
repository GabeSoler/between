# Generated by Django 5.1.1 on 2024-10-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dive_app", "0002_alter_shadow_text_care_plan_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creation",
            name="text_concepts",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="creation",
            name="text_conection",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="creation",
            name="text_craft",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="creation",
            name="text_metaphore",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="creation",
            name="text_sensation",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]