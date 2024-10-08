# Generated by Django 4.2.6 on 2024-08-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CookingStories", "0003_article_author_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="article",
            name="rating_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="topic",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/images/"
            ),
        ),
    ]
