try:
    from cryptography.fernet import Fernet  # type: ignore
except ImportError:
    Fernet = None

import base64
import hashlib

def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_bytes(data, password):
    key = generate_key(password)
    if Fernet is None:
        raise ImportError("cryptography package not found. Install it with: pip install cryptography")

    f = Fernet(key)
    return f.encrypt(data)