from django.db import models


class Play(models.Model):
    title = models.CharField(max_length=100, required=True)
    description = models.TextField(max_length=255)

    class Meta:
        ordering = "title"
        verbose_name_plural = "plays"

    def __str__(self):
        return f"{self.title} (id = {self.id})"

