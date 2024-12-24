# Vendor Management System

A Django-based vendor management system with dynamic schema generation.

## Features

- Vendor submission form
- Admin approval system
- Dynamic schema generation based on vendor services
- Document upload and management
- Admin dashboard

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Initial Setup

1. Log in to the admin interface at `/admin`
2. Create ServiceType entries with appropriate schema fields
   Example schema fields for IT Services:
   ```json
   [
     {"name": "tech_stack", "type": "TEXT"},
     {"name": "experience_years", "type": "INTEGER"},
     {"name": "certification", "type": "TEXT"}
   ]
   ```

## Usage

1. Vendors can submit their information through the main page
2. Admins can review submissions in the admin dashboard
3. Upon approval, a custom schema is generated for the vendor
4. Rejected vendors receive a reason for rejection

## Schema Generation

The system automatically generates tables based on the vendor's services when approved. Each service type has its own schema definition stored in the ServiceType model.