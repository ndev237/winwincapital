# contact/admin.py
from django.contrib import admin
from .models import ContactRequest, ClientApplicationRequest, Newsletter


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'subject', 'status', 'created_at']
    list_filter = ['status', 'subject', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'message']
    list_editable = ['status']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Contact', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Demande', {
            'fields': ('subject', 'message')
        }),
        ('Suivi', {
            'fields': ('status', 'assigned_to', 'notes', 'resolved_at')
        }),
        ('Informations', {
            'fields': ('consent_data_processing', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at', 'updated_at']


@admin.register(ClientApplicationRequest)
class ClientApplicationRequestAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'need', 'preferred_agency', 'status', 'created_at']
    list_filter = ['status', 'need', 'preferred_agency', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_editable = ['status']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Informations personnelles', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Demande', {
            'fields': ('need', 'preferred_agency', 'additional_info')
        }),
        ('Suivi', {
            'fields': ('status', 'appointment_date', 'assigned_to', 'notes')
        }),
        ('Informations', {
            'fields': ('consent_data_processing', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at', 'updated_at']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'is_active', 'subscribed_at']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email', 'first_name']
    list_editable = ['is_active']
    date_hierarchy = 'subscribed_at'

    readonly_fields = ['subscribed_at']
