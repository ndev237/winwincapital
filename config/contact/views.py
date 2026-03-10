from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, ClientApplicationForm, NewsletterForm


class ContactView(FormView):
    """General contact form view"""
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        instance = form.save()

        # Envoi email à contact@winwincapital.africa
        try:
            sujet = f"[Contact] {instance.get_subject_display()} - {instance.first_name} {instance.last_name}"
            corps = f"""
Nouveau message de contact reçu sur winwincapital.africa

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFORMATIONS DU CONTACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nom        : {instance.last_name}
Prénom     : {instance.first_name}
Email      : {instance.email}
Téléphone  : {instance.phone or 'Non renseigné'}
Sujet      : {instance.get_subject_display()}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MESSAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{instance.message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ce message a été envoyé depuis le formulaire de contact du site winwincapital.africa
            """
            send_mail(
                subject=sujet,
                message=corps,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            # Email de confirmation au visiteur
            if instance.email:
                corps_visiteur = f"""
Bonjour {instance.first_name},

Nous avons bien reçu votre message et nous vous en remercions.

Notre équipe vous contactera dans les plus brefs délais.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WIN WIN CAPITAL
La finance qui crée de la valeur partagée
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tél : +237 621 77 71 11
Email : contact@winwincapital.africa
Lun–Ven : 8h–16h30 | Sam : 12h30
                """
                send_mail(
                    subject="Win Win Capital - Votre message a bien été reçu",
                    message=corps_visiteur,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[instance.email],
                    fail_silently=True,
                )
        except Exception as e:
            # L'email échoue silencieusement, le formulaire est quand même sauvegardé
            pass

        messages.success(
            self.request,
            _("Votre message a été envoyé avec succès. Nous vous contacterons dans les plus brefs délais.")
        )
        return super().form_valid(form)


class BecomeClientView(FormView):
    """Client application form view"""
    template_name = 'contact/become_client.html'
    form_class = ClientApplicationForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        instance = form.save()

        # Envoi email à contact@winwincapital.africa
        try:
            sujet = f"[Nouveau client] {instance.get_need_display()} - {instance.first_name} {instance.last_name}"
            corps = f"""
Nouvelle demande client reçue sur winwincapital.africa

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFORMATIONS DU PROSPECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nom        : {instance.last_name}
Prénom     : {instance.first_name}
Email      : {instance.email or 'Non renseigné'}
Téléphone  : {instance.phone}
Besoin     : {instance.get_need_display()}
Agence     : {instance.get_preferred_agency_display() if instance.preferred_agency else 'Non renseignée'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFORMATIONS COMPLÉMENTAIRES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{instance.additional_info or 'Aucune information complémentaire'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ce message a été envoyé depuis le formulaire "Devenir client" du site winwincapital.africa
            """
            send_mail(
                subject=sujet,
                message=corps,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            # Email de confirmation au prospect
            if instance.email:
                corps_prospect = f"""
Bonjour {instance.first_name},

Nous avons bien reçu votre demande pour devenir client chez Win Win Capital.

Un conseiller vous contactera prochainement au {instance.phone} pour fixer un rendez-vous.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RÉCAPITULATIF DE VOTRE DEMANDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Besoin     : {instance.get_need_display()}
Agence     : {instance.get_preferred_agency_display() if instance.preferred_agency else 'Non renseignée'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WIN WIN CAPITAL
La finance qui crée de la valeur partagée
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tél : +237 621 77 71 11
Email : contact@winwincapital.africa
Lun–Ven : 8h–16h30 | Sam : 12h30
                """
                send_mail(
                    subject="Win Win Capital - Votre demande a bien été reçue",
                    message=corps_prospect,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[instance.email],
                    fail_silently=True,
                )
        except Exception as e:
            pass

        messages.success(
            self.request,
            _("Votre demande a été enregistrée. Un conseiller vous contactera prochainement pour fixer un rendez-vous.")
        )
        return super().form_valid(form)


class SuccessView(TemplateView):
    """Success page after form submission"""
    template_name = 'contact/success.html'