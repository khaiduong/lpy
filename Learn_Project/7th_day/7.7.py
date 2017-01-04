class Character():
	def __init__(self, name):
		self.name = name
		self.health = 100 
		self.mana = 1000
	def __str__(self):
		return '%s: %s - %s' %(self.name, self.health, self.mana)
	def say(self):
		pass

class DamPhai(Character):
	def dam(self):
		print(self.name + 'dam dam dam')

class DapPhai(Character):
	def dap(self):
		print(self.name + 'dap dap dap')


a = DamPhai('Supperman').dam()
b = DapPhai('Batman').dap()


