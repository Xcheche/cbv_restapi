# Generated by Django 5.0.8 on 2024-10-22 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("score", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
