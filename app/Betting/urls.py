

from django.contrib import admin
from django.urls import path
from auth.views import send_sms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-message', send_sms, name='send sms')
]
