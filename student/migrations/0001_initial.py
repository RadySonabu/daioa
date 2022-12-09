# Generated by Django 4.1.4 on 2022-12-09 05:34

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(max_length=255)),
                ("middle_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("age", models.IntegerField()),
                ("scholar", models.BooleanField(default=False)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
            ],
        ),
    ]
