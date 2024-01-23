# Generated by Django 5.0 on 2024-01-10 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemInfo",
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
                ("item_name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="veg_images")),
            ],
        ),
        migrations.AlterField(
            model_name="items",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="management.iteminfo"
            ),
        ),
        migrations.DeleteModel(
            name="ItemImages",
        ),
    ]
