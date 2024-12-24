from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.vendor_submit, name='vendor_submit'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('after-vendor-submit/', views.after_vendor_submit, name='after_vendor_submit'),
    path('approved-vendors/', views.approved_vendors, name='approved_vendors'),
]

