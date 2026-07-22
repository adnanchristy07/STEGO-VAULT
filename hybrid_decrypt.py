from cryptography.fernet import Fernet
from crypto_rsa.decrypt_rsa import decrypt_with_private_key

def hybrid_decrypt(combined_data):

    encrypted_aes_key, encrypted_file = combined_data.split(b":::")

    # Recover AES key using RSA private key
    aes_key = decrypt_with_private_key(encrypted_aes_key)

    # Decrypt file using AES key
    cipher = Fernet(aes_key)
    decrypted_file = cipher.decrypt(encrypted_file)

    return decrypted_file