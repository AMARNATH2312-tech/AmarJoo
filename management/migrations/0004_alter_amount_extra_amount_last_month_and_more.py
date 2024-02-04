# Generated by Django 5.0.1 on 2024-02-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0003_alter_month_money_spent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="amount",
            name="extra_amount_last_month",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="amount",
            name="last_month_amount_left",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="items",
            name="quantity",
            field=models.CharField(),
        ),
    ]