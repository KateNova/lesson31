# Generated by Django 4.1.1 on 2022-11-04 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0008_alter_ad_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="description",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="ad", name="price", field=models.PositiveIntegerField(),
        ),
    ]
