# pages/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class Page(models.Model):
    """Model for static institutional pages"""
    title = models.CharField(_("Titre"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    content = models.TextField(_("Contenu"))
    meta_description = models.CharField(_("Meta description"), max_length=160, blank=True)
    is_published = models.BooleanField(_("Publié"), default=True)
    created_at = models.DateTimeField(_("Créé le"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Modifié le"), auto_now=True)

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
        ordering = ['title']

    def __str__(self):
        return self.title


class Partner(models.Model):
    """Model for institutional partners"""
    CATEGORY_CHOICES = [
        ('financial', _('Partenaire financier')),
        ('academic', _('Partenaire académique')),
        ('training', _('Formation & Employabilité')),
        ('economic', _('Partenaire économique')),
    ]

    name = models.CharField(_("Nom"), max_length=200)
    category = models.CharField(_("Catégorie"), max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(_("Description"), blank=True)
    logo = models.ImageField(_("Logo"), upload_to='partners/', blank=True, null=True)
    website = models.URLField(_("Site web"), blank=True)
    order = models.IntegerField(_("Ordre d'affichage"), default=0)
    is_active = models.BooleanField(_("Actif"), default=True)

    class Meta:
        verbose_name = _("Partenaire")
        verbose_name_plural = _("Partenaires")
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Agency(models.Model):
    """Model for Win Win Capital agencies"""
    name = models.CharField(_("Nom de l'agence"), max_length=200)
    address = models.TextField(_("Adresse"))
    city = models.CharField(_("Ville"), max_length=100)
    phone = models.CharField(_("Téléphone"), max_length=20)
    whatsapp = models.CharField(_("WhatsApp"), max_length=20, blank=True)
    email = models.EmailField(_("Email"))

    # Opening hours
    monday_hours = models.CharField(_("Lundi"), max_length=50, default="8h30 - 17h00")
    tuesday_hours = models.CharField(_("Mardi"), max_length=50, default="8h30 - 17h00")
    wednesday_hours = models.CharField(_("Mercredi"), max_length=50, default="8h30 - 17h00")
    thursday_hours = models.CharField(_("Jeudi"), max_length=50, default="8h30 - 17h00")
    friday_hours = models.CharField(_("Vendredi"), max_length=50, default="8h30 - 17h00")
    saturday_hours = models.CharField(_("Samedi"), max_length=50, default="Fermé")
    sunday_hours = models.CharField(_("Dimanche"), max_length=50, default="Fermé")

    # Location
    latitude = models.DecimalField(_("Latitude"), max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(_("Longitude"), max_digits=9, decimal_places=6, blank=True, null=True)

    is_main = models.BooleanField(_("Agence principale"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    order = models.IntegerField(_("Ordre d'affichage"), default=0)

    class Meta:
        verbose_name = _("Agence")
        verbose_name_plural = _("Agences")
        ordering = ['-is_main', 'order', 'name']

    def __str__(self):
        return f"{self.name} - {self.city}"


class SavingsProduct(models.Model):
    """Model for savings products"""
    name = models.CharField(_("Nom du produit"), max_length=200)
    description = models.TextField(_("Description"))
    features = models.TextField(_("Caractéristiques"), help_text=_("Une caractéristique par ligne"))
    minimum_amount = models.DecimalField(_("Montant minimum"), max_digits=10, decimal_places=2, blank=True, null=True)
    interest_rate = models.CharField(_("Taux d'intérêt"), max_length=50, blank=True)
    icon_class = models.CharField(_("Classe d'icône"), max_length=100, blank=True,
                                  help_text=_("Ex: savings, school, business"))
    order = models.IntegerField(_("Ordre d'affichage"), default=0)
    is_active = models.BooleanField(_("Actif"), default=True)

    class Meta:
        verbose_name = _("Produit d'épargne")
        verbose_name_plural = _("Produits d'épargne")
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class FinancingProduct(models.Model):
    """Model for financing products"""
    name = models.CharField(_("Nom du produit"), max_length=200)
    description = models.TextField(_("Description"))
    features = models.TextField(_("Caractéristiques"), help_text=_("Une caractéristique par ligne"))
    max_amount = models.DecimalField(_("Montant maximum"), max_digits=12, decimal_places=2, blank=True, null=True)
    duration_range = models.CharField(_("Durée"), max_length=100, blank=True)
    interest_rate = models.CharField(_("Taux d'intérêt"), max_length=50, blank=True)
    requirements = models.TextField(_("Conditions d'éligibilité"), blank=True)
    icon_class = models.CharField(_("Classe d'icône"), max_length=100, blank=True)
    order = models.IntegerField(_("Ordre d'affichage"), default=0)
    is_active = models.BooleanField(_("Actif"), default=True)

    class Meta:
        verbose_name = _("Produit de financement")
        verbose_name_plural = _("Produits de financement")
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]

    def get_requirements_list(self):
        return [r.strip() for r in self.requirements.split('\n') if r.strip()]


class Testimonial(models.Model):
    """Model for client testimonials"""
    name = models.CharField(_("Nom"), max_length=200)
    role = models.CharField(_("Fonction/Activité"), max_length=200)
    content = models.TextField(_("Témoignage"))
    photo = models.ImageField(_("Photo"), upload_to='testimonials/', blank=True, null=True)
    is_published = models.BooleanField(_("Publié"), default=True)
    order = models.IntegerField(_("Ordre d'affichage"), default=0)
    created_at = models.DateTimeField(_("Créé le"), auto_now_add=True)

    class Meta:
        verbose_name = _("Témoignage")
        verbose_name_plural = _("Témoignages")
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.role}"
