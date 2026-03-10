from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, ClientApplicationForm, NewsletterForm


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        instance = form.save()
        try:
            sujet = f"[Contact] {instance.get_subject_display()} - {instance.first_name} {instance.last_name}"
            corps = f"""Nouveau message de contact\n\nNom: {instance.last_name}\nPrenom: {instance.first_name}\nEmail: {instance.email}\nTelephone: {instance.phone or 'Non renseigne'}\nSujet: {instance.get_subject_display()}\n\nMessage:\n{instance.message}"""
            send_mail(subject=sujet, message=corps, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[settings.CONTACT_EMAIL], fail_silently=False)
            if instance.email:
                corps_v = f"Bonjour {instance.first_name},\n\nNous avons bien recu votre message.\nNotre equipe vous contactera dans les plus brefs delais.\n\nWin Win Capital\nTel: +237 621 77 71 11"
                send_mail(subject="Win Win Capital - Message bien recu", message=corps_v, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[instance.email], fail_silently=True)
        except Exception as e:
            print(f"ERREUR EMAIL: {str(e)}")
        messages.success(self.request, _("Votre message a ete envoye avec succes. Nous vous contacterons dans les plus brefs delais."))
        return super().form_valid(form)


class BecomeClientView(FormView):
    template_name = 'contact/become_client.html'
    form_class = ClientApplicationForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        instance = form.save()
        try:
            sujet = f"[Nouveau client] {instance.get_need_display()} - {instance.first_name} {instance.last_name}"
            agence = instance.get_preferred_agency_display() if instance.preferred_agency else 'Non renseignee'
            corps = f"""Nouvelle demande client\n\nNom: {instance.last_name}\nPrenom: {instance.first_name}\nEmail: {instance.email or 'Non renseigne'}\nTelephone: {instance.phone}\nBesoin: {instance.get_need_display()}\nAgence: {agence}\n\nInfos complementaires:\n{instance.additional_info or 'Aucune'}"""
            send_mail(subject=sujet, message=corps, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[settings.CONTACT_EMAIL], fail_silently=False)
            if instance.email:
                corps_p = f"Bonjour {instance.first_name},\n\nNous avons bien recu votre demande.\nUn conseiller vous contactera au {instance.phone}.\n\nBesoin: {instance.get_need_display()}\nAgence: {agence}\n\nWin Win Capital\nTel: +237 621 77 71 11"
                send_mail(subject="Win Win Capital - Demande bien recue", message=corps_p, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[instance.email], fail_silently=True)
        except Exception as e:
            print(f"ERREUR EMAIL: {str(e)}")
        messages.success(self.request, _("Votre demande a ete enregistree. Un conseiller vous contactera prochainement pour fixer un rendez-vous."))
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'contact/success.html'