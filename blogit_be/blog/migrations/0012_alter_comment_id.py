# Generated by Django 4.2.5 on 2023-10-14 04:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0011_alter_post_is_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]