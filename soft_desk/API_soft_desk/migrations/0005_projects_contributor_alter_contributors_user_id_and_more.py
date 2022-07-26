# Generated by Django 4.0.5 on 2022-07-24 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('API_soft_desk', '0004_alter_contributors_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='contributor',
            field=models.ManyToManyField(related_name='contributors', through='API_soft_desk.Contributors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id_contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='author_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_id_project', to=settings.AUTH_USER_MODEL),
        ),
    ]
