import os
from Print import Print

class RenderScreen:
	def clear_screen():
		os.system("cls" if os.name == "nt" else "clear")
	
	def InfoScreen():
		RenderScreen.clear_screen()		

	def AuthScreen():
		Printer=Print()
		Printer.bold()

		Printer.red(open("./asciiart","r").read())

		print('\n\n\n')

		Printer.centered("                \033[1;33m(1)\033[0m Sign\033[31m-\033[0mUp","yellow")
		Printer.centered("               \033[1;33m(2)\033[0m Log\033[31m-\033[0mIn","yellow")

		Printer.reset()


	def HomeScreen():
		Printer=Print()
		RenderScreen.clear_screen()

		Printer.bold()
		Printer.centered("SecurePass","green")
		Printer.centered("Password Management System","white")
		Printer.reset()

		print("\t\t\t\t\t     (1) Store Password")
		print("\t\t\t\t\t     (2) Display Password")
		print("\t\t\t\t\t     (3) Display All Passwords")
		print("\t\t\t\t\t     (4) Remove Password")
		print("\t\t\t\t\t     (5) Exit Application")

	def Header(header,color):
		Printer=Print()
		RenderScreen.clear_screen()
		Printer.bold()
		Printer.centered("SecurePass",f"{color}")
		Printer.centered("Password Management System","white")
		print()
		Printer.centered(f"{header}","yellow")
		Printer.reset()
