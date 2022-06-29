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
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
