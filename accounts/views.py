from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import africastalking
from .serializers import USSDCallbackSerializer
from env import config
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password

username = config.USERNAME    # use 'sandbox' for development in the test environment
api_key = config.API_key      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

class USSDCallbackView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = USSDCallbackSerializer(data=request.data)
        if serializer.is_valid():
            session_id = serializer.validated_data.get('sessionId', None)
            service_code = serializer.validated_data.get('serviceCode', None)
            phone_number = serializer.validated_data.get('phoneNumber', None)
            text = serializer.validated_data.get('text', None)

            response = 'END Error'

            if text is None or text == '':
                # Initial request
                response = "CON Welcome! Please choose an option:\n"
                response += "1. Login\n"
                response += "2. Register\n"
            elif text == '1':
                # Login option
                response = "CON Please enter your phone number:\n"
                request.session['action'] = 'login'
            elif request.session.get('action') == 'login' and 'phone_number' not in request.session:
                # Save phone number for login
                request.session['phone_number'] = text
                response = "CON Enter your password:\n"
            elif request.session.get('action') == 'login' and 'phone_number' in request.session:
                # Handle login password
                password = text
                phone_number = request.session['phone_number']
                status=login(phone_number=phone_number, password=password)
                if(status!='success'):
                    response='END Log in failed'
                    del request.session['action']
                    del request.session['phone_number']
                    HttpResponse(response, content_type='text/plain')
                # Add login logic here (e.g., authenticate user)
                response = "CON Login successful!"
                del request.session['action']
                del request.session['phone_number']
            elif text == '2':
                # Register option
                response = "CON Please enter your phone number to register:\n"
                request.session['action'] = 'register'
            elif request.session.get('action') == 'register' and 'phone_number' not in request.session:
                # Save phone number for registration
                request.session['phone_number'] = text
                response = "CON Enter your Username:\n"
            elif request.session.get('action') == 'register' and 'phone_number' not in request.session:
                # Save phone number for registration
                request.session['username'] = text
                response = "CON Enter your password:\n"
            elif request.session.get('action') == 'register' and 'phone_number' in request.session:
                # Handle registration password
                password = text
                phone_number = request.session['phone_number']
                username = request.session['username']
                statusmessage=register(phone_number=phone_number,username=username, password=password, request=request)
                if(statusmessage!='success'):
                    response=f'CON {statusmessage}\n Enter new phone number to register:\n'
                    del request.session['action']
                    del request.session['phone_number']
                    del request.session['username']
                    return HttpResponse(response, content_type='text/plain')
                # Add registration logic here (e.g., create user)
                response = "CON Registration successful! \n Check your phone and Enter OTP Sent"
                
            elif request.session.get('action') == 'register' and 'phone_number' in request.session and 'username' in request.session and 'password' in request.session:
                otp=text
                username=request.session['username']
                username=request.session['password']
                username=request.session['phone_number']
                status=validateotp(username=username, password=password, phone_number=phone_number, otp=otp)
                if(status!='success'):
                    response='END INvalid OTP \n'
                    return HttpResponse(response, content_type='text/plain')
                del request.session['action']
                del request.session['phone_number']
                del request.session['username']
                del request.session['otp']
                pass
            else:
                response = "END Invalid input. Please try again."

            return HttpResponse(response, content_type='text/plain')
        else:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    



def register(phone_number, username, password, request):
    if CustomUser.objects.filter(phone=phone_number).exists():
        return 'Number already registered'  # Phone number already exists
    
    user = CustomUser(phone=phone_number, username=username)
    user.set_password(password)  # Hash the password
    user.save()
    # generate otp
    otp=1
    request.session['otp']=otp

    # send OTP
    return 'success'

def login(phone_number, password):
    try:
        user = CustomUser.objects.get(phone=phone_number)
        if user.check_password(password):
            return 'success'
        return 'Log in Failed'
    except CustomUser.DoesNotExist:
        return 'Log in Failed'
    
def validateotp(username, password, phonenumber, otp):
    # validate
    pass