# Generated by Django 4.2.5 on 2023-10-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0023_remove_post_comments_count_alter_post_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="header_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
