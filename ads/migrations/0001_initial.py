# Generated by Django 4.1.1 on 2022-10-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ad",
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
                ("name", models.CharField(max_length=250)),
                ("price", models.IntegerField()),
                ("description", models.CharField(max_length=2000)),
                ("is_published", models.BooleanField(default=False)),
                ("image", models.ImageField(upload_to="images/")),
            ],
            options={
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=250)),
            ],
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории",},
        ),
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=250)),
                ("lat", models.FloatField()),
                ("ing", models.FloatField()),
            ],
            options={"verbose_name": "Локация", "verbose_name_plural": "Локации",},
        ),
    ]
