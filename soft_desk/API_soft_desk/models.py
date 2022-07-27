from django.conf import settings
from django.db import models


class Projects(models.Model):
    """Model for projects data"""

    CHOICES_TYPE = [
        ("front-end", "front-end"),
        ("back-end", "back-end"),
        ("android", "android"),
        ("iOS", "iOS"),
    ]

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=30, choices=CHOICES_TYPE)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author_id_project",
    )
    contributor = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through="Contributors",
        related_name="contributors",
    )

    def __str__(self):
        """
        get title for show it, in admin pages
        """
        return self.title


class Contributors(models.Model):
    """Model for Contributor"""

    POSSIBILITIES = [("read", "read"), ("total", "total")]
    ROLE = [
        ("auteur", "auteur"),
        ("collaborateur", "collaborateur"),
    ]

    user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_id_contributor",
    )
    project_id = models.ForeignKey(
        to=Projects, on_delete=models.CASCADE, blank=True, null=True
    )
    permission = models.CharField(max_length=10, choices=POSSIBILITIES, null=False, blank=False)
    role = models.CharField(
        max_length=150, choices=ROLE, null=False, blank=False
    )


class Issues(models.Model):
    """Model for Issues"""

    PRIORITY_CHOICES = (
        ("faible", "faible"),
        ("moyen", "moyen"),
        ("urgent", "urgent"),
    )
    TAG_CHOICES = (
        ("bug", "bug"),
        ("amélioration", "amélioration"),
        ("tâche", "tâche"),
    )
    STATUS_CHOICES = (
        ("à faire", "à faire"),
        ("en cours", "en cours"),
        ("terminé", "terminé"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    tag = models.CharField(max_length=15, choices=TAG_CHOICES)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="assignee_issue",
        null=True,
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        get title for show it, in admin pages
        """
        return self.title


class Comments(models.Model):
    """Model for Comments"""

    description = models.CharField(max_length=200)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    issue = models.ForeignKey(to=Issues, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        get title for show it, in admin pages
        """
        return self.description
