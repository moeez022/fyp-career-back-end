# Generated by Django 5.0 on 2024-05-01 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0002_remove_quizformatric_question3_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuizforInter",
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
                (
                    "question1",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Question No.1",
                    ),
                ),
                (
                    "question2",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Question No.2",
                    ),
                ),
            ],
        ),
    ]
