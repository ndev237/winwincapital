# contact/urls.py
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
    path('devenir-client/', views.BecomeClientView.as_view(), name='become_client'),
    path('succes/', views.SuccessView.as_view(), name='success'),
]