# pages/admin.py
from django.contrib import admin
from .models import Page, Partner, Agency, SavingsProduct, FinancingProduct, Testimonial

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published', 'updated_at']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_active', 'order']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'phone', 'is_main', 'is_active', 'order']
    list_filter = ['city', 'is_main', 'is_active']
    search_fields = ['name', 'city', 'address']
    list_editable = ['is_main', 'is_active', 'order']
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'address', 'city', 'phone', 'whatsapp', 'email')
        }),
        ('Horaires d\'ouverture', {
            'fields': ('monday_hours', 'tuesday_hours', 'wednesday_hours',
                      'thursday_hours', 'friday_hours', 'saturday_hours', 'sunday_hours')
        }),
        ('Localisation', {
            'fields': ('latitude', 'longitude')
        }),
        ('Paramètres', {
            'fields': ('is_main', 'is_active', 'order')
        }),
    )


@admin.register(SavingsProduct)
class SavingsProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'minimum_amount', 'interest_rate', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['is_active', 'order']


@admin.register(FinancingProduct)
class FinancingProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'max_amount', 'duration_range', 'interest_rate', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['is_active', 'order']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'is_published', 'order', 'created_at']
    list_filter = ['is_published', 'created_at']
    search_fields = ['name', 'role', 'content']
    list_editable = ['is_published', 'order']

