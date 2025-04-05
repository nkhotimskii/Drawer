from django.db import models


class Project(models.Model):

    name = models.CharField(
        max_length=30
    )
    details = models.CharField(
        max_length=500
    )

    def __str__(self):
        return self.name


class Plan(models.Model):

    content = models.CharField(
        max_length=500
    )
    is_done = models.BooleanField(
        default=False
    )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.content