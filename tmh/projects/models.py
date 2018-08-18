from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
from tmh.users.models import User

class Project(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    ROOM_CHOICES = (
        ('BEDROOM', 'Bedroom'),
        ('LIVING_ROOM', 'Living Room'),
        ('MULTIPURPOSE_ROOM', 'Open Layout'),
        ('STUDIO', 'Studio'),
        ('DINING_ROOM', 'Dining Room'),
        ('HOME_OFFICE', 'Office'),
    )

    room = models.CharField(max_length=100, choices=ROOM_CHOICES)

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

    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    SHARED_WITH_CHOICES = (
        ('MYSELF', 'Myself'),
        ('PARTNER', 'Partner'),
        ('ROOMMATE', 'Roommate(s)'),
        ('FAMILY', 'Family'),
    )
    
    shared_with = models.CharField(max_length=100, choices=SHARED_WITH_CHOICES)

    BUDGET_CHOICES = (
        ('1', '$2k or less'),
        ('2', '$2k - $4k'),
        ('3', '$4k - $6k'),
        ('4', '$4k or more'),
    )
    
    budget = models.CharField(max_length=1, choices=BUDGET_CHOICES)
    
    pet_friendly = models.BooleanField(default=True)
    limited_access = models.BooleanField(default=False)
    style = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    designer_note = models.CharField(max_length=200)
    final_note = models.CharField(max_length=200)
    revision_count = models.IntegerField()

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        '''A string representation of the model.'''
        return self.user.username + "'s " + self.get_room_display()

class ProjectDetail(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    TYPE_CHOICES = (
        ('DRAWING', 'Drawing'),
        ('INSPIRATION', 'Inspiration'),
        ('FURNITURE', 'Existing furniture'),
    )

    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    url = models.TextField(validators=[URLValidator()])