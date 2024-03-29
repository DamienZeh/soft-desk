# Generated by Django 4.0.5 on 2022-07-06 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("API_soft_desk", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Issues",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=500)),
                (
                    "tag",
                    models.CharField(
                        choices=[
                            ("bug", "bug"),
                            ("amélioration", "amélioration"),
                            ("tâche", "tâche"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("faible", "faible"),
                            ("moyen", "moyen"),
                            ("urgent", "urgent"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("à faire", "à faire"),
                            ("en cours", "en cours"),
                            ("terminé", "terminé"),
                        ],
                        max_length=15,
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "assigned_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="assignee_issue",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "author_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="API_soft_desk.projects",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contributors",
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
                    "permission",
                    models.CharField(
                        choices=[("read", "read"), ("total", "total")],
                        max_length=10,
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("auteur", "auteur"),
                            ("responsable", "responsable"),
                            ("manager", "manager"),
                        ],
                        max_length=150,
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="API_soft_desk.projects",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
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
                ("description", models.CharField(max_length=200)),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "author_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "issue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="API_soft_desk.issues",
                    ),
                ),
            ],
        ),
    ]
