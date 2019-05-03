import uuid
from django.db import models
from .project import Project

class ProjectDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='details')
    
    STATUS_CHOICES = (
        ('APPROVED', 'Approved'),
        ('PENDING', 'Pending'),
        ('SUBMITTED', 'Submitted'),
    )

    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    TYPE_CHOICES = (
        ('DRAWING', 'Drawing'),
        ('INSPIRATION', 'Inspiration'),
        ('FURNITURE', 'Existing Furniture'),
        ('CONCEPT', 'Concept'),
        ('FLOOR_PLAN', 'Floor Plan'),
        ('FINAL_SNAPSHOT', 'Final Snapshot')
    )

    type = models.CharField(max_length=100, choices=TYPE_CHOICES)

    def __str__(self):
        '''A string representation of the model.'''
        return self.project.client.username + "'s " + self.get_type_display() + " for " + self.project.room