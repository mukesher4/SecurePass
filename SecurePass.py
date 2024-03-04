import hashlib
import getpass
import os
import time

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

class Print():
	def __init__(self):
		self.colors={"red":31,"yellow":33,"default":0,"underline":4,"white":37,"green":32}
	def red(self,text):
		print("\33[31m"+text)
	def yellow(self,text):
		print("\33[33m"+text)
	def green(self,text):
		print("\33[32m"+text)
	def reset(self):
		print("\33[0m")
	def bold(self):
		print("\33[1m")
	def centered(self,text,color):
		if color=="underline":
			t=f"\33[4m"+text+"\33[0m"
		else:
			t=f"\33[{self.colors[color]}m"+text
		print('{:^115}'.format(t))

count=1

class RenderScreen:
	def InfoScreen():
		# Printer=Print()
		# clear_screen()

		# # Printer.bold()
		# # Printer.centered("19CSE201 - Advanced Programming","red");
		# # print()

		# Printer.centered("Welcome to SecurePass ","yellow")
		# Printer.centered("A Place to Store you passwords securely","default")
		# Printer.reset()

		# print("\n\n\n");
    

		# print("\033[?25l")
		# time.sleep(1.5)
		# print("\33[?25h")

		clear_screen()
		

	def AuthScreen():
		Printer=Print()
		Printer.bold()
		Printer.centered("SecurePass","yellow")
		Printer.centered("Password Management System","white")
		Printer.reset()

		Printer.centered(" (1) Sign-Up","default")
		Printer.centered("(2) Log-In","default")

		print('\n\n')

	def HomeScreen():
		Printer=Print()
		clear_screen()

		Printer.bold()
		Printer.centered("SecurePass","green")
		Printer.centered("Password Management System","white")
		Printer.reset()

		print("\t\t\t\t\t     (1) Store Password")
		print("\t\t\t\t\t     (2) Display Password")
		print("\t\t\t\t\t     (3) Exit Application")

	def Header(header,color):
		Printer=Print()
		clear_screen()
		Printer.bold()
		Printer.centered("SecurePass",f"{color}")
		Printer.centered("Password Management System","white")
		print()
		Printer.centered(f"{header}","yellow")
		Printer.reset()

class PasswordChecker:
	@staticmethod
	def check_upper(password):
		global count
		if not any(char.isupper() for char in password):
			print(f"\n({count}) Minimum One \033[0;31mUppercase\033[0m Character")
			count+=1
		return any(char.isupper() for char in password)

	@staticmethod
	def check_lower(password):
		global count
		if not any(char.islower() for char in password):
			print(f"\n({count}) Minimum One \033[0;31mLowercase\033[0m Character")
			count+=1            
		return any(char.islower() for char in password)

	@staticmethod
	def check_digit(password):
		global count
		if not any(char.isdigit() for char in password):
			print(f"\n({count}) Minimum One \033[0;31mDigit\033[0m");
			count+=1

		return any(char.isdigit() for char in password)

	@staticmethod
	def check_special(password):
		global count
		if not any(not char.isalnum() or char.isspace() for char in password):
			print(f"\n({count}) Minimum One \033[0;31mSpecial Character\033[0m")
			count+=1
		return any(not char.isalnum() or char.isspace() for char in password)

	@staticmethod
	def check_length(password):
		global count
		if not len(password) >= 8:
			print(f"\n({count}) Minimum \033[0;31mLength 8\033[0m")
			count+=1
		return len(password) >= 8

	@staticmethod
	def is_password_valid(password):
		global count
		count = 1
		bool_upper=PasswordChecker.check_upper(password)
		bool_lower=PasswordChecker.check_lower(password)
		bool_digit=PasswordChecker.check_digit(password)
		bool_special=PasswordChecker.check_special(password)
		bool_length=PasswordChecker.check_length(password)
		return (bool_upper and bool_lower and bool_digit and bool_special and bool_length)
		Print.reset()

	@staticmethod
	def calculate_md5(message):
		return hashlib.md5(message.encode()).hexdigest()

class EncryptionUtility:
	@staticmethod
	def decryption(cipher, key):
		decrypted = ""
		for i in range(len(cipher)):
			decrypted += chr((ord(cipher[i]) - ord(key[i % len(key)]) + 128) % 128)
		return decrypted

	@staticmethod
	def encryption(plain, key):
		cipher = ""
		for i in range(len(plain)):
			cipher += chr((ord(plain[i]) + ord(key[i % len(key)])) % 128)
		return cipher

class PasswordManager:
	def __init__(self):
		self.account_type = ""
		self.AccountType = {1 : "Website" , 2 : "App" , 3 : "Mail"} 

	def add_password(self, m_user, m_key):
		global account_type_choice
		print("\t\t\t\t\t\t(1) Website")
		print("\t\t\t\t\t\t(2) Application")
		print("\t\t\t\t\t\t(3) E-Mail")
		print("\t\t\t\t\t\t(4) Return back")

		try:
			account_type_choice = int(input("\n>>> Enter Your \33[1m\33[33mChoice\33[0m: "))
		except:
			account_type_choice=-1        
		
		while not 1<=account_type_choice<=4:
			Printer.bold()
			Printer.red("Invalid choice. Try Again")
			Printer.reset()
			try:
				account_type_choice = int(input(">>> Enter Your \33[1m\33[33mChoice\33[0m: "))
			except:
				pass 

		if account_type_choice==4:
			return

		else:
			self.account_type = input(f"\n>>> Enter \33[1m\33[33m{self.AccountType[account_type_choice]}\33[0m : ")

			username = input("\n>>> Enter \33[1m\33[33mUsername\33[0m: ")

			password = getpass.getpass(prompt="\n>>> Enter \33[1m\33[33mPassword\33[0m: ")

			while not PasswordChecker.is_password_valid(password):
				password = getpass.getpass(prompt="\n>>> Enter \33[1m\33[33mPassword\33[0m Again: ")

			with open("userinfo.txt", "a") as user_file:
				user_file.write(
					f"{account_type_choice}~^~{self.account_type}~^~{username}~^~{m_key}~^~{EncryptionUtility.encryption(password, m_key)}\n"
				)

	def display(self, username):
		global account_type_choice
		number_of_records=0
		record=[]
		try:
			with open("userinfo.txt", "r") as file:
				lines = file.readlines()
		except:
			return False
		for line in lines:
			data = line.split("~^~")
			if data[2] == username:
				number_of_records+=1
				decrypted_password = EncryptionUtility.decryption(data[4], data[3])[:-1]
				record.append([number_of_records,self.AccountType[int(data[0])],data[1],decrypted_password])

		if len(record)!=0:
			print()
			print("                       ----------------------------------------------------------------------")
			print("                       | S.No |    Account Type    |      Service       |      Password     |")
			print("                       ----------------------------------------------------------------------")        
			for i in range(len(record)):
				print(f"                       | {record[i][0]:<3}  | {record[i][1]:<18} | {record[i][2]:<18} | {record[i][3]:<17} |")
				print("                       ----------------------------------------------------------------------")
			print()
			return True
		else:
			return False

class MasterCredentialsManager:
	def is_master_username_exists(self, username, master_info):
		return any(user_info[0] == username for user_info in master_info)

	def is_master_credentials_exists(self, username, password, master_info):
		for user_info in master_info:
			if user_info[0] == username and user_info[2] == password:
				return user_info[1]
		return None

	def data_from_master(self, master_info):
		try:
			with open("master.txt", "r") as file:
				lines = file.readlines()

			for line in lines:
				data = line.split()
				master_info.append(data)
		except:
			with open("master.txt", "w"):
				pass

if __name__ == "__main__":

	Printer=Print()

	RenderScreen.InfoScreen()

	master_info = []
	MCM_instance = MasterCredentialsManager()
	MCM_instance.data_from_master(master_info)

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
		while MCM_instance.is_master_username_exists(m_user, master_info):
			Printer.bold()
			Printer.red("Username already exists")
			Printer.reset()
			m_user = input(">>> Enter \33[1m\33[33mMaster Username\33[0m again: ")

		m_key = input("\n>>> Enter \33[1m\33[33mMaster Key\33[0m: ")
		m_password = getpass.getpass(prompt="\nEnter \33[1m\33[33mMaster Password\33[0m: ")

		m_length = len(m_password)

		while not PasswordChecker.is_password_valid(m_password):
			m_password = getpass.getpass(prompt="\n>>> Enter \33[1m\33[33mMaster Password\33[0m Again: ")
			m_length = len(m_password)

		encrypted_signup_pass = PasswordChecker.calculate_md5(m_password)

		with open("master.txt", "a") as master_file:
			master_file.write(f"{m_user} {m_key} {encrypted_signup_pass}\n")

	elif m_choice == 2:

		RenderScreen.Header("Log-In","yellow")

		m_user = input("\n>>> Enter \33[1m\33[33mMaster Username\33[0m: ")
		m_password = getpass.getpass(prompt="\n>>> Enter \33[1m\33[33mMaster Password\33[0m: ")

		encrypted_login_pass = PasswordChecker.calculate_md5(m_password)

		m_key = MCM_instance.is_master_credentials_exists(m_user, encrypted_login_pass, master_info)

		if m_key is not None:
			Printer.bold()
			input(f"\33[1m\33[32mWelcome {m_user}, Press Enter to Continue\33[0m ")
			Printer.reset()
		else:
			Printer.bold()
			Printer.red("Wrong Credentials, Exiting... \n")
			exit()
	else:
		Printer.bold()
		Printer.red("Invalid choice. Exiting...\n")
		exit()

	password_manager = PasswordManager()

	while True:
		RenderScreen.HomeScreen()

		try:
			choice = int(input("\n>>> Enter Your \33[1m\33[33mChoice\33[0m: "))
		except:
			choice = -1

		if choice == 1:
			RenderScreen.Header("Store Password","green")
			
			password_manager.add_password(m_user, m_key)

		elif choice == 2:
			RenderScreen.Header("Display Passwords","green")

			username_to_display = input(">>> Enter \33[1m\33[33mUsername\33[0m to be displayed: ")
			if not password_manager.display(username_to_display):
				Printer.bold()
				Printer.red("No such Records found")
				Printer.reset()
			input(">>> Press \33[1m\33[33mEnter\33[0m to continue ")

		elif choice == 3:
			Printer.bold()
			Printer.red("Exiting...\n")
			exit()

		else:
			Printer.bold()
			Printer.red("Invalid choice. Try Again")
			Printer.reset()
			input(">>> Press \33[1m\33[33mEnter\33[0m to continue ")
