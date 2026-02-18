# contact/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactRequest(models.Model):
    """Model for general contact requests"""
    STATUS_CHOICES = [
        ('new', _('Nouveau')),
        ('in_progress', _('En cours')),
        ('resolved', _('Résolu')),
        ('closed', _('Fermé')),
    ]

    SUBJECT_CHOICES = [
        ('info', _('Demande d\'information')),
        ('account', _('Ouverture de compte')),
        ('credit', _('Demande de crédit')),
        ('complaint', _('Réclamation')),
        ('partnership', _('Partenariat')),
        ('other', _('Autre')),
    ]

    # Contact info
    first_name = models.CharField(_("Prénom"), max_length=100)
    last_name = models.CharField(_("Nom"), max_length=100)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Téléphone"), max_length=20)

    # Request details
    subject = models.CharField(_("Sujet"), max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField(_("Message"))

    # Follow-up
    status = models.CharField(_("Statut"), max_length=20, choices=STATUS_CHOICES, default='new')
    notes = models.TextField(_("Notes internes"), blank=True)
    assigned_to = models.CharField(_("Assigné à"), max_length=100, blank=True)

    # Tracking
    created_at = models.DateTimeField(_("Reçu le"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Modifié le"), auto_now=True)
    resolved_at = models.DateTimeField(_("Résolu le"), blank=True, null=True)

    # Privacy
    consent_data_processing = models.BooleanField(_("Consentement traitement des données"), default=False)

    class Meta:
        verbose_name = _("Demande de contact")
        verbose_name_plural = _("Demandes de contact")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_subject_display()} - {self.first_name} {self.last_name}"


class ClientApplicationRequest(models.Model):
    """Model for client application requests (Devenir client)"""
    STATUS_CHOICES = [
        ('pending', _('En attente')),
        ('contacted', _('Contacté')),
        ('appointment', _('Rendez-vous planifié')),
        ('completed', _('Dossier ouvert')),
        ('cancelled', _('Annulé')),
    ]

    NEED_CHOICES = [
        ('savings', _('Ouvrir un compte d\'épargne')),
        ('current', _('Ouvrir un compte courant')),
        ('credit_personal', _('Demande de crédit personnel')),
        ('credit_school', _('Demande de crédit scolaire')),
        ('credit_business', _('Demande de crédit activité/PME')),
        ('info', _('Demande d\'information')),
    ]

    # Personal info
    first_name = models.CharField(_("Prénom"), max_length=100)
    last_name = models.CharField(_("Nom"), max_length=100)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Téléphone"), max_length=20)

    # Request
    need = models.CharField(_("Besoin"), max_length=30, choices=NEED_CHOICES)
    preferred_agency = models.ForeignKey(
        'pages.Agency',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Agence souhaitée")
    )
    additional_info = models.TextField(_("Informations complémentaires"), blank=True)

    # Follow-up
    status = models.CharField(_("Statut"), max_length=20, choices=STATUS_CHOICES, default='pending')
    appointment_date = models.DateTimeField(_("Date du rendez-vous"), blank=True, null=True)
    notes = models.TextField(_("Notes internes"), blank=True)
    assigned_to = models.CharField(_("Assigné à"), max_length=100, blank=True)

    # Tracking
    created_at = models.DateTimeField(_("Créé le"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Modifié le"), auto_now=True)

    # Privacy
    consent_data_processing = models.BooleanField(_("Consentement traitement des données"), default=False)

    class Meta:
        verbose_name = _("Demande client")
        verbose_name_plural = _("Demandes clients")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_need_display()}"


class Newsletter(models.Model):
    """Model for newsletter subscriptions"""
    email = models.EmailField(_("Email"), unique=True)
    first_name = models.CharField(_("Prénom"), max_length=100, blank=True)
    is_active = models.BooleanField(_("Actif"), default=True)
    subscribed_at = models.DateTimeField(_("Inscrit le"), auto_now_add=True)
    unsubscribed_at = models.DateTimeField(_("Désinscrit le"), blank=True, null=True)

    class Meta:
        verbose_name = _("Abonné newsletter")
        verbose_name_plural = _("Abonnés newsletter")
        ordering = ['-subscribed_at']

    def __str__(self):
        return self.email
