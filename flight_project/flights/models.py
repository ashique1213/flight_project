from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} ({self.position})"


class Route(models.Model):
    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='source_routes')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination_routes')
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return f"{self.source.code} ➜ {self.destination.code} ({self.duration} mins)"
