from django.db import models
from tmh.users.models import User
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    style = models.CharField(max_length=200)
    room_type = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    designer_note = models.CharField(max_length=200)
    final_note = models.CharField(max_length=200)
    revision_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        """A string representation of the model."""
        return self.room_type