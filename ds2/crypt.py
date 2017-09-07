import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.fernet import Fernet

def fencrypt(msg, key):
	cs = Fernet(key)
	return cs.encrypt(msg)

def fdecrypt(msg, key):
	cs = Fernet(key)
	return cs.decrypt(msg)

def encrypt(msg, key, iv):
	padder = padding.PKCS7(128).padder()
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
	padded_data = padder.update(msg)
	padded_data += padder.finalize()
	encryptor = cipher.encryptor()
	return (encryptor.update(padded_data) + encryptor.finalize())

def decrypt(msg, key, iv):
	unpadder = padding.PKCS7(128).unpadder()
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
	decryptor = cipher.decryptor()
	padded_data = decryptor.update(msg) + decryptor.finalize()
	data = unpadder.update(padded_data)
	return data + unpadder.finalize()
