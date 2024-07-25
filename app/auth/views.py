from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from africastalking_service import sms

def send_sms(request):
    recipients = ["+254111204383"]  # Replace with actual phone numbers
    message = "Hello from Django and Africa's Talking!"

    try:
        response = sms.send(message, recipients)
        return JsonResponse(response, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
