# Generated by Django 5.0.3 on 2024-12-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_alter_vendor_services_offered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='schema_fields',
            field=models.JSONField(),
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='services_offered',
        ),
        migrations.AddField(
            model_name='vendor',
            name='services_offered',
            field=models.CharField(choices=[('it_services', 'It Services'), ('logistics', 'Logistics')], default='logistics', max_length=20),
        ),
    ]
