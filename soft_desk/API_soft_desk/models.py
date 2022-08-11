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
        null=True,
        db_column="author_user_id",
    )
    contributor = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through="Contributors",
        related_name="contributions",
    )

    class Meta:

        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Contributors(models.Model):
    """Model for Contributor"""

    POSSIBILITIES = [("lecture_seule", "lecture_seule"), ("total", "total")]
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
        db_column="user_id",
    )
    project_id = models.ForeignKey(
        to=Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_column="project_id",
    )
    permission = models.CharField(
        max_length=13,
        choices=POSSIBILITIES,
        null=False,
        blank=False,
        default="lecture_seule",
    )
    role = models.CharField(
        max_length=150,
        choices=ROLE,
        null=False,
        blank=False,
        default="collaborateur",
    )

    class Meta:

        verbose_name = "Contributor"
        verbose_name_plural = "Contributors"


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
    project_id = models.ForeignKey(
        to=Projects, on_delete=models.CASCADE, db_column="project_id"
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    author_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        db_column="author_user_id",
    )
    assignee_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="assignee_issue",
        null=True,
        db_column="assignee_user_id",
    )
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Issue"
        verbose_name_plural = "Issues"


class Comments(models.Model):
    """Model for Comments"""

    description = models.CharField(max_length=200)
    author_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        db_column="author_user_id",
    )
    issue_id = models.ForeignKey(
        to=Issues, on_delete=models.CASCADE, null=True, db_column="issue_id"
    )
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Comment"
        verbose_name_plural = "Comments"
