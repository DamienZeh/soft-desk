# Generated by Django 4.0.5 on 2022-08-01 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "API_soft_desk",
            "0011_rename_assigned_user_issues_assignee_user_id_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="comments",
            old_name="author_user",
            new_name="author_user_id",
        ),
        migrations.RenameField(
            model_name="comments",
            old_name="issue",
            new_name="issue_id",
        ),
    ]