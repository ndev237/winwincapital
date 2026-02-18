from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactRequest, ClientApplicationRequest, Newsletter

class ContactForm(forms.ModelForm):
    """General contact form"""
    class Meta:
        model = ContactRequest
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message', 'consent_data_processing']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'placeholder': _('Prénom')
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'placeholder': _('Nom')
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'placeholder': _('Email')
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'placeholder': _('+237 XXX XXX XXX')
            }),
            'subject': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'rows': 5,
                'placeholder': _('Votre message...')
            }),
            'consent_data_processing': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-win-green focus:ring-win-green border-gray-300 rounded'
            })
        }


class ClientApplicationForm(forms.ModelForm):
    """Client application form (Devenir client)"""
    class Meta:
        model = ClientApplicationRequest
        fields = ['first_name', 'last_name', 'email', 'phone', 'need', 'preferred_agency', 'additional_info', 'consent_data_processing']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'placeholder': _('Prénom')
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'placeholder': _('Nom')
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'placeholder': _('Email')
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'placeholder': _('+237 XXX XXX XXX')
            }),
            'need': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green'
            }),
            'preferred_agency': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green'
            }),
            'additional_info': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'rows': 4,
                'placeholder': _('Informations complémentaires (optionnel)...')
            }),
            'consent_data_processing': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-win-green focus:ring-win-green border-gray-300 rounded'
            })
        }


class NewsletterForm(forms.ModelForm):
    """Newsletter subscription form"""
    class Meta:
        model = Newsletter
        fields = ['email', 'first_name']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'placeholder': _('Votre email')
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-win-green',
                'placeholder': _('Prénom (optionnel)')
            })
        }
