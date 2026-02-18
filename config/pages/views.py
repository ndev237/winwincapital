# pages/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Page, Partner, Agency, SavingsProduct, FinancingProduct, Testimonial


class HomeView(TemplateView):
    """Homepage view"""
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_testimonials'] = Testimonial.objects.filter(is_published=True)[:3]
        return context


class AboutView(TemplateView):
    """About page view"""
    template_name = 'pages/about.html'


class GovernanceView(TemplateView):
    """Governance page view"""
    template_name = 'pages/governance.html'


class SavingsView(ListView):
    """Savings products page"""
    model = SavingsProduct
    template_name = 'pages/savings.html'
    context_object_name = 'products'

    def get_queryset(self):
        return SavingsProduct.objects.filter(is_active=True)


class FinancingView(ListView):
    """Financing products page"""
    model = FinancingProduct
    template_name = 'pages/financing.html'
    context_object_name = 'products'

    def get_queryset(self):
        return FinancingProduct.objects.filter(is_active=True)


class ImpactView(TemplateView):
    """Impact page view"""
    template_name = 'pages/impact.html'


class PartnersView(ListView):
    """Partners page"""
    model = Partner
    template_name = 'pages/partners.html'
    context_object_name = 'partners'

    def get_queryset(self):
        return Partner.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Group partners by category
        context['financial_partners'] = self.get_queryset().filter(category='financial')
        context['academic_partners'] = self.get_queryset().filter(category='academic')
        context['training_partners'] = self.get_queryset().filter(category='training')
        context['economic_partners'] = self.get_queryset().filter(category='economic')
        return context


class AgenciesView(ListView):
    """Agencies page"""
    model = Agency
    template_name = 'pages/agencies.html'
    context_object_name = 'agencies'

    def get_queryset(self):
        return Agency.objects.filter(is_active=True)


class ComplianceView(TemplateView):
    """Compliance and client protection page"""
    template_name = 'pages/compliance.html'


class PrivacyPolicyView(TemplateView):
    """Privacy policy page"""
    template_name = 'pages/privacy.html'


class TermsView(TemplateView):
    """Terms and conditions page"""
    template_name = 'pages/terms.html'


class PageDetailView(DetailView):
    """Generic page detail view"""
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

    def get_queryset(self):
        return Page.objects.filter(is_published=True)
