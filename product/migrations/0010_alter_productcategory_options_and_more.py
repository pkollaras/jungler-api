# Generated by Django 5.0.4 on 2024-04-11 11:43
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "product",
            "0009_remove_product_product_pro_hits_19ae26_btree_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productcategory",
            options={
                "ordering": ["-sort_order"],
                "verbose_name": "Product Category",
                "verbose_name_plural": "Product Categories",
            },
        ),
        migrations.AlterModelOptions(
            name="productimage",
            options={
                "ordering": ["-sort_order"],
                "verbose_name": "Product Image",
                "verbose_name_plural": "Product Images",
            },
        ),
    ]
