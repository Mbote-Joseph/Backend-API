# Generated by Django 4.1 on 2022-08-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("farmerName", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=200)),
                ("price", models.FloatField()),
                ("quantity", models.IntegerField()),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
    ]