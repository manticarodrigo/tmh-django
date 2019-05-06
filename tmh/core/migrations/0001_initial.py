# Generated by Django 2.0.8 on 2019-05-06 22:06

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tmh.core.models.message
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='users')),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
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
                ('revision_count', models.IntegerField(default=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
                ('designer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='designer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='details')),
                ('status', models.CharField(choices=[('APPROVED', 'Approved'), ('PENDING', 'Pending'), ('SUBMITTED', 'Submitted')], max_length=100)),
                ('type', models.CharField(choices=[('DRAWING', 'Drawing'), ('INSPIRATION', 'Inspiration'), ('FURNITURE', 'Existing Furniture'), ('CONCEPT', 'Concept'), ('FLOOR_PLAN', 'Floor Plan'), ('FINAL_SNAPSHOT', 'Final Snapshot')], max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='details')),
                ('status', models.CharField(choices=[('APPROVED', 'Approved'), ('PENDING', 'Pending'), ('SUBMITTED', 'Submitted'), ('REQUEST_ALTERNATIVE', 'Request Alternative'), ('ALTERNATE_READY', 'Alternate Ready')], max_length=100)),
                ('make', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('inspiration', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('lat', models.DecimalField(decimal_places=20, max_digits=25)),
                ('lng', models.DecimalField(decimal_places=20, max_digits=25)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alternatives', to='core.ProjectItem')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(validators=[tmh.core.models.message.validate_message_content])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Project')),
            ],
        ),
    ]
