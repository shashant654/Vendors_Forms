from django.db import models
from django.contrib.auth.models import User
from django.db import connection

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    schema_fields = models.JSONField()

    def __str__(self):
        return self.name

class Vendor(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    service_choices = [
        ('it_services', 'It Services'),
        ('logistics','Logistics')
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)
    # services_offered = models.ManyToManyField(ServiceType)
    services_offered = models.CharField(max_length=20, choices=service_choices, default='logistics')
    documents = models.FileField(upload_to='vendor_documents/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    rejection_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ServiceOffered(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="services")
    name = models.CharField(max_length=100)
    schema_fields = models.JSONField()
    services_offered_by_vendor = models.TextField()  # Add a descriptive field

    def __str__(self):
        return f"{self.name} by {self.vendor.name}"

