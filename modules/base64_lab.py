import base64

def decode_base64(encoded_text):
    try:
        decoded = base64.b64decode(encoded_text).decode('utf-8')
        return decoded
    except:
        return "Invalid Base64 Input"