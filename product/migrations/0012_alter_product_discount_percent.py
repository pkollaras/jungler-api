# Generated by Django 5.0.4 on 2024-04-17 15:43
from decimal import Decimal

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0011_alter_productcategory_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="discount_percent",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0"),
                max_digits=11,
                verbose_name="Discount Percent",
            ),
        ),
    ]