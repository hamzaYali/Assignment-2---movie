from django.db import models
from django.utils import timezone

class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=360)
    year = models.IntegerField(blank=False, null=False)
    rating = models.IntegerField(blank=False, null=False)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()