import africastalking
from django.conf import settings

africastalking.initialize(settings.AFRICAS_TALKING_USERNAME, settings.AFRICAS_TALKING_API_KEY)

sms = africastalking.SMS
