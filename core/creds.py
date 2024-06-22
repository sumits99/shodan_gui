from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import pathlib 

default_private_key_fpath = pathlib.Path.home().joinpath(".ssh/id_rsa")

class CredStore:
    def __init__(self, private_key_path=default_private_key_fpath):
        self.private_key_path= private_key_path
        self.private_key = self.load_private_key()
        self.data = {}
        
    # Load the private key
    def load_private_key(self):
        with open(self.private_key_path, "rb") as key_file:
            private_key = serialization.load_ssh_private_key(key_file.read(), password=None)
        return private_key

    # Encrypt data
    def encrypt_data(self, data):
        encrypted = self.private_key.public_key().encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted

    # Decrypt data
    def decrypt_data(self, encrypted_data):
        decrypted = self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode()

    # Save encrypted credentials to file
    def save_encrypted_data(self,file_path, encrypted_data):
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

    # Load encrypted data from file
    def load_encrypted_data(self,file_path):
        if pathlib.Path(file_path).exists():
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
            return encrypted_data
        return False


# # Path to your SSH private key
# private_key_path = "~/.ssh/id_rsa"

# # Load your SSH private key
# private_key = load_private_key(private_key_path)

# # Your data to be encrypted
# data = "your_sensitive_data"

# # Encrypt the data
# encrypted_data = encrypt_data(private_key, data)

# # Save encrypted data to file
# save_encrypted_data("data.enc", encrypted_data)

# # Load encrypted data from file
# loaded_encrypted_data = load_encrypted_data("data.enc")

# # Decrypt the data
# decrypted_data = decrypt_data(private_key, loaded_encrypted_data)

# print(f"Decrypted Data: {decrypted_data}")
