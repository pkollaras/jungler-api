# Generated by Django 5.1.4 on 2024-12-31 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_notificationuser_notificatio_user_id_f8507b_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='link',
            field=models.URLField(blank=True, default='', verbose_name='Link'),
        ),
    ]
