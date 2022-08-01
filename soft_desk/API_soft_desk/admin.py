from django.contrib import admin
from .models import Contributors, Projects, Issues, Comments


class ProjectAdmin(admin.ModelAdmin):
    """Show project's info in admin"""

    list_display = ("title", "description", "type", "author_user_id")


class IssueAdmin(admin.ModelAdmin):
    """Show project's info in admin"""

    list_display = (
        "title",
        "description",
        "tag",
        "priority",
        "project_id",
        "status",
        "author_user_id",
        "assignee_user_id",
        "created_time",
    )


class CommentAdmin(admin.ModelAdmin):
    """Show project's info in admin"""

    list_display = (
        "description",
        "author_user_id",
        "issue_id",
        "created_time",
    )


admin.site.register(Projects, ProjectAdmin)
admin.site.register(Issues, IssueAdmin)
admin.site.register(Comments, CommentAdmin)
