from django.db import models


class Play(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=255)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "plays"

    def __str__(self):
        return f"{self.title} (id = {self.id})"

