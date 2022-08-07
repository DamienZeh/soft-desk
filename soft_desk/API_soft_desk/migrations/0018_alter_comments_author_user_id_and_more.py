# Generated by Django 4.0.5 on 2022-08-07 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API_soft_desk', '0017_alter_projects_author_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author_user_id',
            field=models.ForeignKey(db_column='author_user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='issue_id',
            field=models.ForeignKey(db_column='issue_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='API_soft_desk.issues'),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='project_id',
            field=models.ForeignKey(blank=True, db_column='project_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='API_soft_desk.projects'),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='user_id',
            field=models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id_contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issues',
            name='assignee_user_id',
            field=models.ForeignKey(db_column='assignee_user_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignee_issue', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issues',
            name='author_user_id',
            field=models.ForeignKey(db_column='author_user_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issues',
            name='project_id',
            field=models.ForeignKey(db_column='project_id', on_delete=django.db.models.deletion.CASCADE, to='API_soft_desk.projects'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='author_user_id',
            field=models.ForeignKey(db_column='author_user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_id_project', to=settings.AUTH_USER_MODEL),
        ),
    ]