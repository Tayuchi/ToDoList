# Generated by Django 4.1.3 on 2022-12-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=30, verbose_name="タスク名")),
                ("description", models.TextField(blank=True, verbose_name="詳細")),
                ("deadline", models.DateField(verbose_name="締切")),
            ],
        ),
    ]
