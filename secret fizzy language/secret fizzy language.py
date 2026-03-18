
""" 
SECRET MESSAGING BY FIZZY

zeros added for confusing and also the message written is reversed (from right to left). 

for decoding just remove all zeros and reverse the string to get the message

 """






# normal message to fizzy language


import random

class SecretEncoder:

    def __init__(self, message):
        self.message = message

    def encode(self):
        reversed_msg = self.message[::-1]
        secret = ""
        for i in range(len(reversed_msg)):
            secret += reversed_msg[i]
            if i < len(reversed_msg) - 1:
                secret += "01" * random.randint(1, 3)
        return secret

msg = input("Enter your secret message to encode it: ")
encoder = SecretEncoder(msg)

secret = encoder.encode()
print("Secret Message:", secret)




# decoding fizzy language


class Translate:

    def __init__(self,msg):
        self.msg=msg

    def decoding(self):
        cleaned = self.msg.replace("0", "").replace("1", "")
        decoded = cleaned[::-1]
        print("Decoded Message:", decoded)


hidden_msg=input("Ente your secret message to decode it : ")    
ob=Translate(hidden_msg)

ob.decoding()



