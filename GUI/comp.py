class Comp():

	def __init__(self):
		self.name = ""
		self.path = ""
		self.opt1 = []
		self.opt2 = []


	def setName(self, name):
		self.name = name
	def getName(self):
		return self.name
	def setPath(self, path):
		self.path = path
	def getPath(self):
		return self.path
	def addOpt1(self, t):
		self.opt1.append(t)
	def addOpt2(self, t):
		self.opt2.append(t)
	def getOpt1(self):
		return self.opt1
	def getOpt2(self):
		return self.opt2
	def __str__(self):
		str = "{}=path:{}".format(self.name, self.path)
		if len(self.opt1) != 0:
			str = ("{}, opt1:{}".format(str, self.opt1))
		if len(self.opt2) != 0:
			str = ("{}, opt2:{}".format(str, self.opt2))	
		return str			
