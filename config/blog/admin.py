# blog/admin.py
from django.contrib import admin
from .models import Category, BlogPost, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'is_published', 'is_featured', 'published_date', 'views_count']
    list_filter = ['is_published', 'is_featured', 'category', 'published_date']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    list_editable = ['is_published', 'is_featured']

    fieldsets = (
        ('Contenu', {
            'fields': ('title', 'slug', 'category', 'excerpt', 'content', 'featured_image')
        }),
        ('SEO', {
            'fields': ('meta_description',)
        }),
        ('Publication', {
            'fields': ('author', 'is_published', 'is_featured', 'published_date')
        }),
        ('Statistiques', {
            'fields': ('views_count',),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['views_count']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
