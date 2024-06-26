from EncryptionUtility import EncryptionUtility
from PasswordChecker import PasswordChecker
from integrateFirebase import IntegrateFirebase
from Print import Print
import getpass, random

class PasswordManager:
	def __init__(self):
		self.account_type = ""
		self.AccountType = {1 : "Website" , 2 : "App" , 3 : "Mail"} 

	def add_password(self, authHash, decryptedVault, FireBase, EncryptionUtil):
		print("\t\t\t\t\t\t\033[1;33m(1)\033[0m Website")
		print("\t\t\t\t\t\t\033[1;33m(2)\033[0m Application")
		print("\t\t\t\t\t\t\033[1;33m(3)\033[0m E\033[1;31m-\033[0mMail")
		print("\t\t\t\t\t\t\033[1;33m(4)\033[0m Return\033[1;31m_\033[0mback")

		try:
			account_type_choice = int(input("\n>>> Enter Your \33[1m\33[33mChoice\33[0m: "))
		except:
			account_type_choice=-1        
		
		while not 1<=account_type_choice<=4:
			Printer=Print()

			Printer.bold()
			Printer.red("Invalid choice. Try Again")
			Printer.reset()
			try:
				account_type_choice = int(input(">>> Enter Your \33[1m\33[33mChoice\33[0m: "))
			except:
				pass 

		if account_type_choice==4:
			pass

		else:
			self.account_type = input(f"\n>>> Enter \33[1m\33[33m{self.AccountType[account_type_choice]}\33[0m : ")

			username = input("\n>>> Enter \33[1m\33[33mUsername\33[0m: ")
			print()
			print("\033[1m\033[34m(Press 'g' or 'G' to generate a strong Password)\033[0m")
			password = getpass.getpass(prompt=">>> Enter \33[1m\33[33mPassword\33[0m: ")

			if password == 'g' or password == 'G':
				password = self.generatePassword(8)
				print()
				print("\033[1m\033[32mGenerated Password successfully\033[0m")

			decryptedVault.append(f"{account_type_choice}~^~{self.account_type}~^~{username}~^~{password}")

			FireBase.insertData(EncryptionUtil.encryption(decryptedVault))

		return decryptedVault

	def removePassword(self, sno, decryptedVault, FireBase, EncryptionUtil):
		if len(decryptedVault) >= sno:
			del decryptedVault[sno-1]
			FireBase.insertData(EncryptionUtil.encryption(decryptedVault))
			return decryptedVault
		else:
			return None

	def displayAll(self, decryptedVault):
		Printer=Print()

		number_of_records=0
		record=[]
		for line in decryptedVault:
			data = line.split("~^~")
			number_of_records+=1
			password = data[-1]
			record.append([str(number_of_records)+".",data[2],self.AccountType[int(data[0])],data[1],password])

		if len(record)!=0:
			print()
			print("         \033[1;31m--------------------------------------------------------------------------------------------\033[0m")
			print("        \033[1;31m|\033[0m \033[1;34mS.No\033[0m \033[1;31m|\033[0m     \033[1;34mUsername\033[0m       \033[1;31m|\033[0m \033[1;34mAccount Type\033[0m \033[1;31m|\033[0m          \033[1;34mService\033[0m           \033[1;31m|\033[0m      \033[1;34mPassword\033[0m      \033[1;31m|\033[0m")
			print("         \033[1;31m--------------------------------------------------------------------------------------------\033[0m")        
			for i in range(len(record)):
				if record[i][2] == "App": color = Printer.appColor()
				elif record[i][2] == "Mail": color = Printer.mailColor()
				elif record[i][2] == "Website": color = Printer.websiteColor()
				
				print(f"        \033[1;31m|\033[0m {record[i][0]:<3}  \033[1;31m|\033[0m {record[i][1]:<18} \033[1;31m|\033[0m {color}{record[i][2]:<12}\033[0m \033[1;31m|\033[0m {record[i][3]:<26} \033[1;31m|\033[0m {color}{record[i][4]:<18}\033[0m\033[1;31m|\033[0m")
				print("         \033[1;31m--------------------------------------------------------------------------------------------\033[0m")        
			print()
			return True
		else:
			return False

	def display(self, username, decryptedVault):
		Printer=Print()

		number_of_records=0
		record=[]
		for line in decryptedVault:
			data = line.split("~^~")
			if data[2] == username:
				number_of_records+=1
				password = data[-1]
				record.append([str(number_of_records)+".",data[2],self.AccountType[int(data[0])],data[1],password])

		if len(record)!=0:
			print()
			print("         \033[1;31m--------------------------------------------------------------------------------------------\033[0m")
			print("        \033[1;31m|\033[0m \033[1;34mS.No\033[0m \033[1;31m|\033[0m     \033[1;34mUsername\033[0m       \033[1;31m|\033[0m \033[1;34mAccount Type\033[0m \033[1;31m|\033[0m          \033[1;34mService\033[0m           \033[1;31m|\033[0m      \033[1;34mPassword\033[0m      \033[1;31m|\033[0m")
			print("         \033[1;31m--------------------------------------------------------------------------------------------\033[0m")        
			for i in range(len(record)):
				if record[i][2] == "App": color = Printer.appColor()
				elif record[i][2] == "Mail": color = Printer.mailColor()
				elif record[i][2] == "Website": color = Printer.websiteColor()
				
				print(f"        \033[1;31m|\033[0m {record[i][0]:<3}  \033[1;31m|\033[0m {record[i][1]:<18} \033[1;31m|\033[0m {color}{record[i][2]:<12}\033[0m \033[1;31m|\033[0m {record[i][3]:<26} \033[1;31m|\033[0m {color}{record[i][4]:<18}\033[0m\033[1;31m|\033[0m")
				print("         \033[1;31m--------------------------------------------------------------------------------------------\033[0m")        
			print()
			return True
		else:
			return False

	def generateVaultKey(self, m_user, m_pass):
		m_key = m_user+m_pass
		for i in range(10):
			m_key = PasswordChecker.calculate_md5(m_key)
		return m_key

	def generateAuthenticationHash(self, m_key, m_pass):
		authHash = m_key+m_pass
		for i in range(5):
			authHash = PasswordChecker.calculate_md5(authHash)
		return authHash

	def generatePassword(self, lenght):
		pool = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&'()*+,-./:;<=>?@'"""
		
		capChar = pool[:26]
		smallChar = pool[26:52]
		digits = pool[52:62]
		specialChar = pool[62:]
		
		password = [capChar[random.randint(0, len(capChar)-1)],
					smallChar[random.randint(0, len(smallChar)-1)],
					digits[random.randint(0, len(digits)-1)],
					specialChar[random.randint(0, len(specialChar)-1)]]

		while lenght > len(password):
			random.shuffle(password)
			password += pool[random.randint(0, len(pool)-1)] 

		return ''.join(password)