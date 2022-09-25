from cryptography.fernet import Fernet
import base64

def encrypt_password(master_password, password):
    master_password_encoded = base64.urlsafe_b64encode(bytes(master_password, encoding='utf8'))
    fernet = Fernet(master_password_encoded)

    password_encoded = base64.urlsafe_b64encode(bytes(password, encoding='utf8'))

    encrypted_password = fernet.encrypt(password_encoded)

    return encrypted_password

def decrypt():
    pass