# Generated by Django 5.0.6 on 2024-06-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("between_app", "0016_remove_ps_group_image_path_alter_ps_group_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bigtraditions",
            name="cybernetic",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="bigtraditions",
            name="hemeneutic",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="bigtraditions",
            name="phenomenological",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="bigtraditions",
            name="scientific",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="bigtraditions",
            name="spiritual",
            field=models.IntegerField(default=1),
        ),
    ]