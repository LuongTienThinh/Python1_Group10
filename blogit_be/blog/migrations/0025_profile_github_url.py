# Generated by Django 4.2.5 on 2023-10-17 17:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0024_post_header_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="github_url",
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
    ]