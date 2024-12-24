from django import forms
from .models import Vendor, ServiceType

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'email', 'contact_number', 'services_offered', 'documents']

class VendorApprovalForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['status', 'rejection_reason']

    def save(self, commit=True):
        vendor = super().save(commit=False)
        if vendor.status == 'approved' and commit:
            vendor.create_service_schema()
        if commit:
            vendor.save()
        return vendor
