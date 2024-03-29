# Generated by Django 4.0.5 on 2022-08-07 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("API_soft_desk", "0016_alter_comments_author_user_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects",
            name="author_user_id",
            field=models.ForeignKey(
                db_column="emp_id",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author_id_project",
                to=settings.AUTH_USER_MODEL,
                verbose_name="author_user_id",
            ),
        ),
    ]
