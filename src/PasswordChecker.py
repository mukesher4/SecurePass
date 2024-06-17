import hashlib

count = 1

class PasswordChecker:
	def check_upper(password):
		global count
		if not any(char.isupper() for char in password):
			print(f"\n({count}) Minimum One \033[0;31mUppercase\033[0m Character")
			count+=1
		return any(char.isupper() for char in password)

	def check_lower(password):
		global count
		if not any(char.islower() for char in password):
			print(f"\n({count}) Minimum One \033[0;31mLowercase\033[0m Character")
			count+=1            
		return any(char.islower() for char in password)

	def check_digit(password):
		global count
		if not any(char.isdigit() for char in password):
			print(f"\n({count}) Minimum One \033[0;31mDigit\033[0m");
			count+=1

		return any(char.isdigit() for char in password)

	def check_special(password):
		global count
		if not any(not char.isalnum() or char.isspace() for char in password):
			print(f"\n({count}) Minimum One \033[0;31mSpecial Character\033[0m")
			count+=1
		return any(not char.isalnum() or char.isspace() for char in password)

	def check_length(password):
		global count
		if not len(password) >= 8:
			print(f"\n({count}) Minimum \033[0;31mLength 8\033[0m")
			count+=1
		return len(password) >= 8

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

	def calculate_md5(message):
		return hashlib.md5(message.encode()).hexdigest()
