# Generated by Django 5.1.1 on 2024-10-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("between_app", "0004_alter_personalstyle_acceptant_1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bigtraditions",
            name="constructive",
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name="bigtraditions",
            name="cybernetic",
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name="bigtraditions",
            name="hemeneutic",
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name="bigtraditions",
            name="participatory",
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name="bigtraditions",
            name="phenomenological",
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name="bigtraditions",
            name="scientific",
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name="bigtraditions",
            name="spiritual",
            field=models.IntegerField(default=50),
        ),
    ]