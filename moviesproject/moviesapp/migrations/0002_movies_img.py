# Generated by Django 4.1.7 on 2023-03-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("moviesapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movies",
            name="img",
            field=models.ImageField(default="tw4wt", upload_to="gallery"),
            preserve_default=False,
        ),
    ]
