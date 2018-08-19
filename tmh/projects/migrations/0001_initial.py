# Generated by Django 2.0.8 on 2018-08-19 22:59

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('room', models.CharField(choices=[('BEDROOM', 'Bedroom'), ('LIVING_ROOM', 'Living Room'), ('MULTIPURPOSE_ROOM', 'Open Layout'), ('STUDIO', 'Studio'), ('DINING_ROOM', 'Dining Room'), ('HOME_OFFICE', 'Office')], default='BEDROOM', max_length=100)),
                ('status', models.CharField(choices=[('DETAILS', 'Details'), ('DESIGN', 'Design'), ('CONCEPTS', 'Concepts'), ('FLOOR_PLAN', 'Floor Plan'), ('REQUEST_ALTERNATIVES', 'Request Alternatives'), ('ALTERNATIVES_READY', 'Alternatives Ready'), ('FINAL_DELIVERY', 'Final Delivery'), ('SHOPPING_CART', 'Shopping Cart'), ('ESTIMATE_SHIPPING_AND_TAX', 'Estimate Shipping & Tax'), ('CHECKOUT', 'Checkout'), ('ARCHIVED', 'Archived')], default='DETAILS', max_length=100)),
                ('shared_with', models.CharField(choices=[('MYSELF', 'Myself'), ('PARTNER', 'Partner'), ('ROOMMATE', 'Roommate(s)'), ('FAMILY', 'Family')], default='MYSELF', max_length=100)),
                ('budget', models.CharField(choices=[('1', '$2k or less'), ('2', '$2k - $4k'), ('3', '$4k - $6k'), ('4', '$4k or more')], default='1', max_length=1)),
                ('pet_friendly', models.BooleanField(default=True)),
                ('limited_access', models.BooleanField(default=False)),
                ('style', models.CharField(blank=True, max_length=200)),
                ('video_url', models.TextField(blank=True, validators=[django.core.validators.URLValidator()])),
                ('zipcode', models.CharField(blank=True, max_length=200)),
                ('designer_note', models.CharField(blank=True, max_length=200)),
                ('final_note', models.CharField(blank=True, max_length=200)),
                ('revision_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
