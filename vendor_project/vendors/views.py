from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import *
from .forms import VendorForm, VendorApprovalForm

def is_admin(user):
    return user.is_superuser

def vendor_submit(request):
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            vendor = form.save()
            messages.success(request, 'Vendor submission successful! Waiting for admin approval.')

            return redirect('after_vendor_submit')
    else:
        form = VendorForm()
    return render(request, 'vendors/vendor_submit.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    vendors = Vendor.objects.all().order_by('-created_at')
    return render(request, 'vendors/admin_dashboard.html', {'vendors': vendors})

def after_vendor_submit(request):
    items = Vendor.objects.all()
    return render(request, 'vendors/after_vendor_submit.html',{'items':items})

@login_required
def approved_vendors(request):
    approved_vendors = Vendor.objects.filter(status='approved').order_by('-updated_at')
    return render(request, 'vendors/approved_vendors.html', {'approved_vendors': approved_vendors})




