from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    f = Fernet(key)
    return f.encrypt(message.encode())

if __name__ == '__main__':
    key = generate_key()
    print("Key:", key.decode())
    encrypted = encrypt_message(key, "Secret CTF flag")
    print("Encrypted:", encrypted.decode())
