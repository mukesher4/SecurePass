import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class IntegrateFirebase:
	def __init__(self, master_user=None, authHash=None):
		self.collection_name = 'Credentials'
		filelocation = open("./credentialsLocation.txt", "r").read().strip()
		self.cred = credentials.Certificate(filelocation)

		if not firebase_admin._apps:
			firebase_admin.initialize_app(self.cred)
		
		self.db = firestore.client()
		self.collection_ref = self.db.collection(self.collection_name)
		
		self.m_user = master_user
		self.authHash = authHash		

	def searchForMasterUsername(self, m_user):
		docs = self.collection_ref.stream()

		for doc in docs:
			doc_dict = doc.to_dict()
			if doc_dict['m_userHash'] == m_user:
				return True

		return False

	def insertData(self, encryptedCreds):
		data = 	{
			'm_userHash': self.m_user, 
			'encryptedCreds': encryptedCreds
		}

		doc_ref = self.collection_ref.document(self.authHash)
		doc_ref.set(data)

	def getVault(self, key):
		doc_ref = self.collection_ref.document(self.authHash)
		
		doc = doc_ref.get()

		if doc.exists:
			return doc.to_dict()['encryptedCreds']

		else:
			return None