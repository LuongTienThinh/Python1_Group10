# Generated by Django 4.2.5 on 2023-10-06 15:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0003_category_post_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="blog_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
