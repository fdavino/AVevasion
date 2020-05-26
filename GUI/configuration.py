from comp import Comp
class Conf():

	def __init__(self):
		self.templatePath = ""
		self.payloadPath = ""
		self.specialCh = ""
		self.placeholderPayload = ""
		self.freq = ""
		self.out = ""
		self.subs = []
		self.comps = []


	def setTemplatePath(self, t):
		self.templatePath = t
	def getTemplatePath(self):
		return self.templatePath
	def setPayloadPath(self, pp):
		self.payloadPath = pp
	def getPayloadPath(self):
		return self.payloadPath
	def setSpecialChar(self, sc):
		self.specialCh = sc
	def getSpecialChar(self):
		return self.specialCh
	def setPlaceholderPayload(self, pl):
		self.placeholderPayload = pl
	def getPlaceholderPayload(self):
		return self.placeholderPayload
	def setFreq(self, f):
		self.freq = f	
	def getFreq(self):
		return self.freq
	def setOut(self, out):
		self.out = out
	def getOut(self):
		return self.out
	def addToSub(self, sub):
		self.subs.append(sub)
	def getSub(self):
		return self.subs
	def addToComp(self, comp):
		self.comps.append(comp)
	def getComp(self):
		return self.comps

	def __str__(self):
		jsonFormat = {"manipulations" : {"template":self.templatePath}}
		jsonFormat["manipulations"]["payload"] = {"path":self.payloadPath, "specialch":self.specialCh, "placeholder":self.placeholderPayload}
		if(self.freq != ""):
			jsonFormat["manipulations"]["payload"]["rate"] = self.freq
		if len(self.subs) > 0:
			jsonFormat["manipulations"]["sub"] = []
			for s in self.subs:
				jsonFormat["manipulations"]["sub"].append({"placeholder":s[0], "str":s[1]})
		if len(self.out) > 0:
			jsonFormat["manipulations"]["out"] = self.out
		if len(self.comps) > 0:
			jsonFormat["compilers"] = {}
			for c in self.comps:
				dic = c.jsonFormat()
				for k in dic:
					jsonFormat["compilers"][k] = dic.get(k)
		return str(jsonFormat)				 												
