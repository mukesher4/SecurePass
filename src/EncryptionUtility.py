from cryptography.fernet import Fernet
import base64

class EncryptionUtility:
	def __init__(self, key):
		self.cipher_suite = Fernet(base64.urlsafe_b64encode(key.encode('utf-8')))

	def decryption(self, cipher, key=None):
		try:
			return self.cipher_suite.decrypt(cipher).decode().split()
		except:
			return []
			
	def encryption(self, plain, key=None):
		plainString = '\n'.join(plain)
		return self.cipher_suite.encrypt(plainString.encode())