# Generated by Django 5.0.6 on 2024-08-08 14:29

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0002_article_article_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=tinymce.models.HTMLField(),
        ),
    ]
