from cryptography.fernet import Fernet
import base64

class EncryptionUtility:
	def __init__(self, key):
		self.cipher_suite = Fernet(base64.urlsafe_b64encode(key.encode('utf-8')))

	def decryption(self, cipher, key):
		try:
			return self.cipher_suite.decrypt(cipher).decode()
		except:
			return ""
			
	def encryption(self, plain, key):
		return self.cipher_suite.encrypt(plain.encode())