import random
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
	def generate_random_ansi(self):
		return random.choice([f"\033[1;3{i}m]" for i in range(0,8)])
	def websiteColor(self):
		return "\033[1;35m"
	def appColor(self):
		return "\033[1;33m"
	def mailColor(self):
		return "\033[1;36m"