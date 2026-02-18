from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .forms import ContactForm, ClientApplicationForm, NewsletterForm


class ContactView(FormView):
    """General contact form view"""
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        form.save()
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
        form.save()
        messages.success(
            self.request,
            _("Votre demande a été enregistrée. Un conseiller vous contactera prochainement pour fixer un rendez-vous.")
        )
        return super().form_valid(form)


class SuccessView(TemplateView):
    """Success page after form submission"""
    template_name = 'contact/success.html'
