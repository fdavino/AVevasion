import random
import json

class Manipulator:

	def __init__(self,conf):
		self.conf = conf

	def __checkObF(self, field, container):
		if not field in container:
			print("{} is an obligatory field".format(field))        
			sys.exit(1)	


	def __editPayload(self,payload,sc,rate):
		f = open(payload)
		content = f.read()
		toRet = ""
		byte = ""
		for i in content:
			if i == '\n' or i == None:
				continue
			byte += i
			if len(byte) == 4:
				if random.random() < rate:
					toRet += sc
				toRet += byte
				byte = ""
		return toRet

	def generateSource(self):
		data = json.load(open(self.conf, "r"))

		self.__checkObF("manipulations",data)
		man = data['manipulations']

		self.__checkObF("template",man)
		self.__checkObF("payload",man)
		template = man['template']
		payload = man['payload']

		self.__checkObF("path",payload)
		self.__checkObF("specialch",payload)
		self.__checkObF("placeholder",payload)
		path = payload['path']
		sc = payload['specialch']
		ph = payload['placeholder']
		rate = 0.20
		if "rate" in payload:
			try:
				rate = float(payload['rate'])
				if not(rate >= 0 and rate < 1):
					raise ValueError
			except ValueError:
				print("rate must be float value between (0 and 1]")
		code = open(template,"r")
		code = code.read()
		code = code.replace(ph, self.__editPayload(path,sc,rate))

		if "sub" in man:
			sub = man['sub']
			for s in sub:
				self.__checkObF("placeholder",s)
				self.__checkObF("str",s)
				code = code.replace(s['placeholder'], s['str'])

		f = open("out.c","w")
		f.write(code)