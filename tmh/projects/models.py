from django.db import models
from tmh.users.models import User
from django.utils import timezone

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
        return self.room