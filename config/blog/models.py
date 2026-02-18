# blog/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """Blog post categories"""
    name = models.CharField(_("Nom"), max_length=100)
    slug = models.SlugField(_("Slug"), unique=True)
    description = models.TextField(_("Description"), blank=True)
    order = models.IntegerField(_("Ordre"), default=0)

    class Meta:
        verbose_name = _("Catégorie")
        verbose_name_plural = _("Catégories")
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """Blog posts for financial education and news"""
    title = models.CharField(_("Titre"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Catégorie"),
        related_name='posts'
    )
    excerpt = models.TextField(_("Résumé"), max_length=300)
    content = models.TextField(_("Contenu"))
    featured_image = models.ImageField(
        _("Image mise en avant"),
        upload_to='blog/',
        blank=True,
        null=True
    )

    # SEO
    meta_description = models.CharField(
        _("Meta description"),
        max_length=160,
        blank=True
    )

    # Publishing
    author = models.CharField(_("Auteur"), max_length=100, default="Win Win Capital")
    is_published = models.BooleanField(_("Publié"), default=False)
    is_featured = models.BooleanField(_("Article en vedette"), default=False)
    published_date = models.DateTimeField(_("Date de publication"), blank=True, null=True)

    # Tracking
    views_count = models.IntegerField(_("Nombre de vues"), default=0)
    created_at = models.DateTimeField(_("Créé le"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Modifié le"), auto_now=True)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ['-published_date', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def increment_views(self):
        self.views_count += 1
        self.save(update_fields=['views_count'])


class Tag(models.Model):
    """Tags for blog posts"""
    name = models.CharField(_("Nom"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ['name']

    def __str__(self):
        return self.name
