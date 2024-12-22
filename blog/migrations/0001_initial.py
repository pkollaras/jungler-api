# Generated by Django 4.2.9 on 2024-02-10 14:39
import uuid

import django.core.validators
import django.db.models.deletion
import django.db.models.manager
import parler.fields
import parler.models
import tinymce.models
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogAuthor",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="Website"),
                ),
            ],
            options={
                "verbose_name": "Blog Author",
                "verbose_name_plural": "Blog Authors",
                "ordering": ["-created_at"],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="BlogAuthorTranslation",
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
                (
                    "language_code",
                    models.CharField(db_index=True, max_length=15, verbose_name="Language"),
                ),
                (
                    "bio",
                    models.TextField(blank=True, null=True, verbose_name="Bio"),
                ),
            ],
            options={
                "verbose_name": "Blog Author Translation",
                "db_table": "blog_blogauthor_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="BlogCategory",
            fields=[
                (
                    "sort_order",
                    models.IntegerField(
                        db_index=True,
                        editable=False,
                        null=True,
                        verbose_name="Sort Order",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("slug", models.SlugField(unique=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="uploads/blog/",
                        verbose_name="Image",
                    ),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                (
                    "tree_id",
                    models.PositiveIntegerField(db_index=True, editable=False),
                ),
                ("level", models.PositiveIntegerField(editable=False)),
            ],
            options={
                "verbose_name": "Blog Category",
                "verbose_name_plural": "Blog Categories",
                "ordering": ["sort_order"],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="BlogCategoryTranslation",
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
                (
                    "language_code",
                    models.CharField(db_index=True, max_length=15, verbose_name="Language"),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
            ],
            options={
                "verbose_name": "Blog Category Translation",
                "db_table": "blog_blogcategory_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="BlogComment",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "is_approved",
                    models.BooleanField(default=False, verbose_name="Is Approved"),
                ),
            ],
            options={
                "verbose_name": "Blog Comment",
                "verbose_name_plural": "Blog Comments",
                "ordering": ["-created_at"],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="BlogCommentTranslation",
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
                (
                    "language_code",
                    models.CharField(db_index=True, max_length=15, verbose_name="Language"),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(1)],
                        verbose_name="Content",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blog Comment Translation",
                "db_table": "blog_blogcomment_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "published_at",
                    models.DateTimeField(blank=True, null=True, verbose_name="Published At"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="Is Published"),
                ),
                (
                    "seo_title",
                    models.CharField(
                        blank=True,
                        max_length=70,
                        null=True,
                        verbose_name="Seo Title",
                    ),
                ),
                (
                    "seo_description",
                    models.TextField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="Seo Description",
                    ),
                ),
                (
                    "seo_keywords",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Seo Keywords",
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="uploads/blog/",
                        verbose_name="Image",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("DRAFT", "Draft"),
                            ("PUBLISHED", "Published"),
                            ("ARCHIVED", "Archived"),
                        ],
                        default="DRAFT",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                (
                    "featured",
                    models.BooleanField(default=False, verbose_name="Featured"),
                ),
                (
                    "view_count",
                    models.IntegerField(default=0, verbose_name="View Count"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="blog_post_author",
                        to="blog.blogauthor",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="blog_post_category",
                        to="blog.blogcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blog Post",
                "verbose_name_plural": "Blog Posts",
                "ordering": ["-published_at"],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="BlogTag",
            fields=[
                (
                    "sort_order",
                    models.IntegerField(
                        db_index=True,
                        editable=False,
                        null=True,
                        verbose_name="Sort Order",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "active",
                    models.BooleanField(default=True, verbose_name="Active"),
                ),
            ],
            options={
                "verbose_name": "Blog Tag",
                "verbose_name_plural": "Blog Tags",
                "ordering": ["sort_order"],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
            managers=[
                ("active_tags", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="BlogTagTranslation",
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
                (
                    "language_code",
                    models.CharField(db_index=True, max_length=15, verbose_name="Language"),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(1)],
                        verbose_name="Name",
                    ),
                ),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="blog.blogtag",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blog Tag Translation",
                "db_table": "blog_blogtag_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="BlogPostTranslation",
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
                (
                    "language_code",
                    models.CharField(db_index=True, max_length=15, verbose_name="Language"),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Title",
                    ),
                ),
                (
                    "subtitle",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Subtitle",
                    ),
                ),
                (
                    "body",
                    tinymce.models.HTMLField(blank=True, null=True, verbose_name="Body"),
                ),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="blog.blogpost",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blog Post Translation",
                "db_table": "blog_blogpost_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]