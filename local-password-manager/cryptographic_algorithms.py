from cryptography.fernet import Fernet
import base64

def encrypt_password(master_password, password):
    master_password_encoded = base64.urlsafe_b64encode(bytes(master_password, encoding='utf8'))
    fernet = Fernet(master_password_encoded)
    
    encrypted_password = fernet.encrypt(password.encode())

    return encrypted_password.decode()

def decrypt_password(master_password, password):
    master_password_encoded = base64.urlsafe_b64encode(bytes(master_password, encoding='utf8'))
    fernet = Fernet(master_password_encoded)

    decrypted_password = fernet.decrypt(password.encode()).decode()

    return decrypted_password