import random

def generatePassword(lenght):

	pool = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&'()*+,-./:;<=>?@'"""
	capChar = pool[:26]
	smallChar = pool[26:52]
	digits = pool[52:62]
	specialChar = pool[62:]
	
	password = [capChar[random.randint(0, len(capChar)-1)], smallChar[random.randint(0, len(smallChar)-1)], digits[random.randint(0, len(digits)-1)], specialChar[random.randint(0, len(specialChar)-1)]]

	while lenght > len(password):
		random.shuffle(password)
		password += pool[random.randint(0, len(pool)-1)] 

	return ''.join(password)

print(generatePassword(8))