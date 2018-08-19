import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import URLValidator

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='client'
    )
    designer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='designer'
    )

    ROOM_CHOICES = (
        ('BEDROOM', 'Bedroom'),
        ('LIVING_ROOM', 'Living Room'),
        ('MULTIPURPOSE_ROOM', 'Open Layout'),
        ('STUDIO', 'Studio'),
        ('DINING_ROOM', 'Dining Room'),
        ('HOME_OFFICE', 'Office'),
    )

    room = models.CharField(max_length=100, choices=ROOM_CHOICES, default='BEDROOM')

    STATUS_CHOICES = (
        ('DETAILS', 'Details'),
        ('DESIGN', 'Design'),
        ('CONCEPTS', 'Concepts'),
        ('FLOOR_PLAN', 'Floor Plan'),
        ('REQUEST_ALTERNATIVES', 'Request Alternatives'),
        ('ALTERNATIVES_READY', 'Alternatives Ready'),
        ('FINAL_DELIVERY', 'Final Delivery'),
        ('SHOPPING_CART', 'Shopping Cart'),
        ('ESTIMATE_SHIPPING_AND_TAX', 'Estimate Shipping & Tax'),
        ('CHECKOUT', 'Checkout'),
        ('ARCHIVED', 'Archived'),
    )

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='DETAILS')

    SHARED_WITH_CHOICES = (
        ('MYSELF', 'Myself'),
        ('PARTNER', 'Partner'),
        ('ROOMMATE', 'Roommate(s)'),
        ('FAMILY', 'Family'),
    )
    
    shared_with = models.CharField(max_length=100, choices=SHARED_WITH_CHOICES, default='MYSELF')

    BUDGET_CHOICES = (
        ('1', '$2k or less'),
        ('2', '$2k - $4k'),
        ('3', '$4k - $6k'),
        ('4', '$4k or more'),
    )
    
    budget = models.CharField(max_length=1, choices=BUDGET_CHOICES, default='1')
    
    pet_friendly = models.BooleanField(default=True)
    limited_access = models.BooleanField(default=False)
    style = models.CharField(max_length=200, blank=True)
    video_url = models.TextField(validators=[URLValidator()], blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    designer_note = models.CharField(max_length=200, blank=True)
    final_note = models.CharField(max_length=200, blank=True)
    revision_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        '''A string representation of the model.'''
        return self.client.username + "'s " + self.get_room_display()

class ProjectDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
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
    image = models.ImageField(upload_to='details')

    def __str__(self):
        '''A string representation of the model.'''
        return self.project.client.username + "'s " + self.get_type_display() + " for " + self.project.room