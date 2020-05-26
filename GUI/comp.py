class Comp():

	def __init__(self):
		self.name = ""
		self.path = ""
		self.opt1 = []
		self.opt2 = []

	def __stringToTuple(self, str):
		str = str.replace("(","")	
		str = str.replace(")","")
		str = str.replace(",","")
		return tuple(str)


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
	def jsonFormat(self):
		jsonFormat = {self.name : {"path" : self.path}}
		if len(self.opt1) != 0:
			o1 = jsonFormat[self.name]["options1"] = []
			for item in self.opt1:
				el = {}
				el["name"] = item[0]
				if len(item[1]) > 0:
					el["value"] = item[1]
				o1.append(el)
		if len(self.opt2) != 0:		
			o2 = jsonFormat[self.name]["options2"] = []
			for item in self.opt2:
				el = {}
				el["name"] = item[0]
				if len(item[1]) > 0:
					el["value"] = item[1]
				o2.append(el)	
		return jsonFormat		

	def __str__(self):
		return str(self.jsonFormat())		
