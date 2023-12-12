from django.urls import path
from . import views

urlpatterns = [
    # ... other url patterns ...
    path('contact/new/', views.contact_create, name='contact_create'),
]
