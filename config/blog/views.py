# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost, Category


class BlogListView(ListView):
    """Blog post list view"""
    model = BlogPost
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_published=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if self.kwargs.get('category_slug'):
            context['current_category'] = get_object_or_404(
                Category,
                slug=self.kwargs.get('category_slug')
            )
        context['featured_posts'] = BlogPost.objects.filter(
            is_published=True,
            is_featured=True
        )[:3]
        return context


class BlogDetailView(DetailView):
    """Blog post detail view"""
    model = BlogPost
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

    def get_object(self):
        obj = super().get_object()
        # Increment view count
        obj.increment_views()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Related posts
        context['related_posts'] = BlogPost.objects.filter(
            is_published=True,
            category=self.object.category
        ).exclude(id=self.object.id)[:3]
        return context
