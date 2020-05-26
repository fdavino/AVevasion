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
