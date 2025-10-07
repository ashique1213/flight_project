from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} ({self.name})"


class Route(models.Model):
    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='source_routes')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination_routes')
    position = models.IntegerField(help_text="Position number in the route sequence")
    duration = models.FloatField(help_text="Duration in hours")

    def __str__(self):
        return f"{self.source.code} ➜ {self.destination.code} ({self.duration} hrs)"
