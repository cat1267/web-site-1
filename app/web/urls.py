from django.urls import path
from .views import index, ContactView

urlpatterns = [
    path('', index, name='index'),
    path('contact/', ContactView.as_view(), name='contact_view'),
]
