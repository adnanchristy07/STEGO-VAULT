from cryptography.fernet import Fernet  # type: ignore
import base64
import hashlib

def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def decrypt_bytes(encrypted_data, password):
    key = generate_key(password)
    f = Fernet(key)
    return f.decrypt(encrypted_data)