# urls.py

from django.urls import path
from .views import USSDCallbackView

urlpatterns = [
    path('', USSDCallbackView.as_view(), name='ussd_callback'),
]
