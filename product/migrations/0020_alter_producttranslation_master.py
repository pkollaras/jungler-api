# Generated by Django 5.1.2 on 2024-10-26 00:00
import django.db.models.deletion
import parler.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0019_alter_producttranslation_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producttranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="product.product",
            ),
        ),
    ]
