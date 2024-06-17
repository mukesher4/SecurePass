from integrateFirebase import IntegrateFirebase

class MasterCredentialsManager:
	def is_master_username_exists(self, m_user, FireBase):
		return FireBase.searchForMasterUsername(m_user)

	def is_master_credentials_exists(self, authHash, FireBase):
		return FireBase.getVault(authHash)
