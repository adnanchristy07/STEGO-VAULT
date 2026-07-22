from cryptography.fernet import Fernet
from crypto_rsa.encrypt_rsa import encrypt_with_public_key

def hybrid_encrypt(file_data):

    # Generate AES key
    aes_key = Fernet.generate_key()

    # Encrypt file using AES
    cipher = Fernet(aes_key)
    encrypted_file = cipher.encrypt(file_data)

    # Encrypt AES key using RSA public key
    encrypted_aes_key = encrypt_with_public_key(aes_key)

    return encrypted_aes_key + b":::" + encrypted_file