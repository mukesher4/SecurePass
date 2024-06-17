from Print import Print; from RenderScreen import RenderScreen; from PasswordChecker import PasswordChecker; from EncryptionUtility import EncryptionUtility; from PasswordManager import PasswordManager; from MasterCredentialsManager import MasterCredentialsManager; from integrateFirebase import IntegrateFirebase
import getpass

if __name__ == "__main__":
	Printer = Print()
	MCM_instance = MasterCredentialsManager()
	password_manager = PasswordManager()

	RenderScreen.InfoScreen()
	RenderScreen.AuthScreen()

	try:
		m_choice = int(input(">>> Enter Your \33[1m\33[33mChoice\33[0m: "))
	except:
		Printer.bold()
		Printer.red("Invalid choice. Exiting...\n")
		exit()

	if m_choice == 1:
		RenderScreen.Header("Sign-Up","yellow")

		m_user = input("\n>>> Enter \33[1m\33[33mMaster Username\33[0m: ")
		FireBase = IntegrateFirebase()
		while MCM_instance.is_master_username_exists(m_user, FireBase):
			Printer.bold()
			Printer.red("Username already exists")
			Printer.reset()
			m_user = input(">>> Enter \33[1m\33[33mMaster Username\33[0m again: ")

		m_password = getpass.getpass(prompt="\n>>> Enter \33[1m\33[33mMaster Password\33[0m: ")

		m_length = len(m_password)

		while not PasswordChecker.is_password_valid(m_password):
			m_password = getpass.getpass(prompt="\n>>> Enter \33[1m\33[33mMaster Password\33[0m Again: ")
			m_length = len(m_password)

		decryptedVault = ""
		m_key = password_manager.generateVaultKey(m_user, m_password)

		authHash = password_manager.generateAuthenticationHash(m_key, m_password)
		
		EncryptionUtil = EncryptionUtility(m_key)	
		FireBase = IntegrateFirebase(PasswordChecker.calculate_md5(m_user), authHash)
		FireBase.insertData("")

	elif m_choice == 2:

		RenderScreen.Header("Log-In","yellow")

		m_user = input("\n>>> Enter \33[1m\33[33mMaster Username\33[0m: ")
		m_password = getpass.getpass(prompt="\n>>> Enter \33[1m\33[33mMaster Password\33[0m: ")
		m_key = password_manager.generateVaultKey(m_user, m_password)

		authHash = password_manager.generateAuthenticationHash(m_key, m_password)

		FireBase = IntegrateFirebase(PasswordChecker.calculate_md5(m_user), authHash)
		vault = MCM_instance.is_master_credentials_exists(authHash, FireBase)

		if vault is not None:
			Printer.bold()
			input(f"\33[1m\33[32mWelcome {m_user}, Press Enter to Continue\33[0m ")
			EncryptionUtil = EncryptionUtility(m_key)
			decryptedVault = EncryptionUtil.decryption(vault, m_key)
			Printer.reset()
		else:
			Printer.bold()
			Printer.red("Wrong Credentials, Exiting... \n")
			exit()
	
	else:
		Printer.bold()
		Printer.red("Invalid choice. Exiting...\n")
		exit()
	
	while True:
		RenderScreen.HomeScreen()
		try:
			choice = int(input("\n>>> Enter Your \33[1m\33[33mChoice\33[0m: "))
		except:
			choice = -1

		if choice == 1:
			RenderScreen.Header("Store Password","green")
			
			decryptedVault = password_manager.add_password(authHash, m_key, decryptedVault, FireBase, EncryptionUtil)

		elif choice == 2:
			RenderScreen.Header("Display Passwords","green")

			username_to_display = input(">>> Enter \33[1m\33[33mUsername\33[0m to be displayed: ")
			if not password_manager.display(username_to_display, decryptedVault):
				Printer.bold()
				Printer.red("No such Records found")
				Printer.reset()
			input(">>> Press \33[1m\33[33mEnter\33[0m to continue ")

		elif choice == 3:
			RenderScreen.Header("Display All Passwords","green")

			if not password_manager.displayAll(decryptedVault):
				Printer.bold()
				Printer.red("No such Records found")
				Printer.reset()
			input(">>> Press \33[1m\33[33mEnter\33[0m to continue ")			

		elif choice == 4:
			RenderScreen.Header("Remove Password","green")

			if not password_manager.displayAll(decryptedVault):
				Printer.bold()
				Printer.red("No such Records found")
				Printer.reset()
				input(">>> Press \33[1m\33[33mEnter\33[0m to continue ")			
			else:
				sno = input(">>> Select S.no to \033[1m\033[31mremove\033[0m Password ")
				if sno != "":
					recoveredVault = password_manager.removePassword(int(sno), decryptedVault, FireBase, EncryptionUtil, m_key)
					if recoveredVault != None:
						decryptedVault = recoveredVault
						print()
						print("\033[1m\033[32mRemoved Password successfully\033[0m")
						print()
						
						input(">>> Press \33[1m\33[33mEnter\33[0m to continue ")			
					else:
						print()
						print("\033[1m\033[31mError in Removing Password\033[0m")
						print()
						input(">>> Press \33[1m\33[33mEnter\33[0m to continue ")			

		elif choice == 5:
			Printer.bold()
			Printer.red("Exiting...\n")
			exit()

		else:
			Printer.bold()
			Printer.red("Invalid choice. Try Again")
			Printer.reset()
			input(">>> Press \33[1m\33[33mEnter\33[0m to continue ")
