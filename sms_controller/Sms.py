import africastalking

# TODO: Initialize Africa's Talking

africastalking.initialize(
    username='sandbox',
    api_key='atsk_dec77e70915af371ad80b4f2323471474b1a40fcf2ca61ba2e7e720c63aae0fadaf38b99'
)

sms = africastalking.SMS

class send_sms():

    def send(self):
        
        #TODO: Send message
        def sending(self):
            # Set the numbers in international format
            recipients = ["+254114883285"]
            # Set your message
            message = "Hello your Authentication Code is ";
            # Set your shortCode or senderId
            sender = "78980"
            try:
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Houston, we have a problem: {e}')
