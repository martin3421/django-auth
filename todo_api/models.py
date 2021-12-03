import datetime

from django.utils import timezone
from django.db import models
from django.conf import settings
from django.urls import reverse

class Task(models.Model):
    title = models.CharField(max_length=140)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name="todo_created_by",
        on_delete=models.CASCADE,
    )
    note = models.TextField(blank=True, null=True)
    priority = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
