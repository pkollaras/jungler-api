# Generated by Django 5.1.4 on 2024-12-31 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_alter_producttranslation_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='seo_description',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='Seo Description'),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='seo_keywords',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Seo Keywords'),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='seo_title',
            field=models.CharField(blank=True, default='', max_length=70, verbose_name='Seo Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_description',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='Seo Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_keywords',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Seo Keywords'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_title',
            field=models.CharField(blank=True, default='', max_length=70, verbose_name='Seo Title'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='seo_description',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='Seo Description'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='seo_keywords',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Seo Keywords'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='seo_title',
            field=models.CharField(blank=True, default='', max_length=70, verbose_name='Seo Title'),
        ),
        migrations.AlterField(
            model_name='producttranslation',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Name'),
        ),
    ]
