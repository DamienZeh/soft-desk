# Generated by Django 4.0.5 on 2022-08-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("API_soft_desk", "0019_alter_contributors_permission_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issues",
            name="created_time",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="['%b %d %Y']"
            ),
        ),
    ]
