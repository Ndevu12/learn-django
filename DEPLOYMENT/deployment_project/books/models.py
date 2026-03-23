from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user with role-based access control."""

    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        EDITOR = 'editor', 'Editor'
        VIEWER = 'viewer', 'Viewer'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.VIEWER,
    )

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    @property
    def is_editor(self):
        return self.role in (self.Role.ADMIN, self.Role.EDITOR)

    def __str__(self):
        return f'{self.username} ({self.role})'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    pub_date = models.DateField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books',
    )

    def __str__(self):
        return self.title
