# Generated by Django 5.0.6 on 2024-07-07 14:34
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("slider", "0005_alter_slide_image_alter_slider_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slide",
            name="slider",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="slides", to="slider.slider"
            ),
        ),
    ]
