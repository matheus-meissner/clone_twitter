# Generated by Django 5.1.3 on 2024-12-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField(max_length=255)),
                ("msg", models.TextField(max_length=255)),
                ("dt", models.TextField(max_length=255)),
                ("hour", models.TextField(max_length=255)),
            ],
        ),
    ]
