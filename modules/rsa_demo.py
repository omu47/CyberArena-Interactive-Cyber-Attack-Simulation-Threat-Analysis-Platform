from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

key = RSA.generate(2048)

public_key = key.publickey()

cipher = PKCS1_OAEP.new(public_key)

def encrypt_message(message):

    encrypted = cipher.encrypt(message.encode())

    return base64.b64encode(encrypted).decode()