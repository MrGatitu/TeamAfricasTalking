import random
import string

class Service:

    CHARACTERS = string.digits
    OTP_LENGTH = 6

    def generate_otp(self):
        otp = ''.join(random.choice(self.CHARACTERS) for _ in range(self.OTP_LENGTH))
        return otp

service = Service()

AuthCode = service.generate_otp()
print(service.generate_otp())
