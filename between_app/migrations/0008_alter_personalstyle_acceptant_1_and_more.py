# Generated by Django 5.1.5 on 2025-03-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("between_app", "0007_personalstyle_therapist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalstyle",
            name="acceptant_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="becoming_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="belonging_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="challenger_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="containment_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="development_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="divider_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="extensive_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="follower_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="individuation_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="intensive_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
        migrations.AlterField(
            model_name="personalstyle",
            name="propositive_1",
            field=models.IntegerField(
                default=50,
                help_text="Left rejection and right support for the statement",
            ),
        ),
    ]
