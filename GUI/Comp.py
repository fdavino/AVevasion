class Comp():
	name = ""
	path = ""
	opt1 = []
	opt2 = []

	def __init__(self):
		pass

	def setName(self, name):
		self.name = name
	def getName(self):
		return self.name
	def setPath(self, path):
		self.path = path
	def getPath(self):
		return self.path
	def addOpt1(self, t):
		opt1.append(t)
	def addOpt2(self, t):
		opt2.append(t)
	def getOpt1(self):
		return opt1
	def getOpt2(self):
		return opt2	
