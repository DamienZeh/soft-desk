# Generated by Django 4.0.5 on 2022-07-27 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "API_soft_desk",
            "0005_projects_contributor_alter_contributors_user_id_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projects",
            name="contributor",
        ),
    ]
