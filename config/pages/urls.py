# pages/urls.py
from tempfile import template

from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomeView.as_view(template_name='home.html'), name='home'),
    path('qui-sommes-nous/', views.AboutView.as_view(), name='about'),
    path('gouvernance/', views.GovernanceView.as_view(), name='governance'),
    path('comptes-epargne/', views.SavingsView.as_view(), name='savings'),
    path('solutions-financement/', views.FinancingView.as_view(), name='financing'),
    path('notre-impact/', views.ImpactView.as_view(), name='impact'),
    path('nos-partenaires/', views.PartnersView.as_view(), name='partners'),
    path('agences/', views.AgenciesView.as_view(), name='agencies'),
    path('protection-client/', views.ComplianceView.as_view(), name='compliance'),
    path('politique-confidentialite/', views.PrivacyPolicyView.as_view(), name='privacy'),
    path('conditions-utilisation/', views.TermsView.as_view(), name='terms'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),
]
