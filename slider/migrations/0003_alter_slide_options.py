# Generated by Django 5.0.4 on 2024-04-11 11:43
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("slider", "0002_slide_slide_created_at_idx_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="slide",
            options={
                "ordering": ["-sort_order"],
                "verbose_name": "Slide",
                "verbose_name_plural": "Slides",
            },
        ),
    ]
