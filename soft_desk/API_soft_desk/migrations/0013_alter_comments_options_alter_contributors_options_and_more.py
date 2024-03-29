# Generated by Django 4.0.5 on 2022-08-05 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "API_soft_desk",
            "0012_rename_author_user_comments_author_user_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comments",
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
        migrations.AlterModelOptions(
            name="contributors",
            options={
                "verbose_name": "Contributor",
                "verbose_name_plural": "Contributors",
            },
        ),
        migrations.AlterModelOptions(
            name="issues",
            options={"verbose_name": "Issue", "verbose_name_plural": "Issues"},
        ),
        migrations.AlterModelOptions(
            name="projects",
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
            },
        ),
    ]
