from django.db import models
from django.utils import timezone
from datetime import date


class Child(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    admission_date = models.DateField()
    photo = models.ImageField(upload_to='child_photos', default='default_child_photo.jpg')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name


from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Donor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    amount_donated = models.PositiveIntegerField()

    def __str__(self):
        return self.name

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject



class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title


from django.contrib.auth.models import User


     

class Donation(models.Model):
    donor_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateField(default=date.today)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.donor_name} donated {self.amount}'







