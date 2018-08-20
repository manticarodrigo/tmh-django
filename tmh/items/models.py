import uuid
from django.db import models
from django.core.validators import URLValidator
from tmh.projects.models import Project

class ProjectItem(models.Model):
    # unique id is ommitted to use
    # autofield as number increment

    # auto fields
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # foreign key fields
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self',
        related_name='alternatives',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    
    # image fields
    image = models.ImageField(upload_to='details')

    # choice fields
    STATUS_CHOICES = (
        ('APPROVED', 'Approved'),
        ('PENDING', 'Pending'),
        ('SUBMITTED', 'Submitted'),
        ('REQUEST_ALTERNATIVE', 'Request Alternative'),
        ('ALTERNATE_READY', 'Alternate Ready')
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    # other fields
    make = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    inspiration = models.TextField(validators=[URLValidator()])
    lat = models.DecimalField(max_digits=25, decimal_places=20)
    lng = models.DecimalField(max_digits=25, decimal_places=20)

    def __str__(self):
        '''A string representation of the model.'''
        return self.project.client.username + "'s " + self.make + " for " + self.project.room