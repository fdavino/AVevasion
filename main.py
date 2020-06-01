import sys
sys.path.append("Component")
sys.path.append("Driver")
sys.path.append("GUI")
from compEngine import CompilationEngine
from virusTotal import VirusTotal
from manipulator import Manipulator
from gui import Gui


conf = ""
clear = False
gui = False

def usage():
	print("usage: python3 main.py")
	print("\t(--conf | -c) configuration file")
	print("\t[--clear | -C] remove folders of precedent executions")
	print("\t[--gui | -G] start the program GUI")
	sys.exit(1)

def manageFlag():
	global conf
	global clear
	global gui
	some = True
	i = 1
	while i < len(sys.argv) and some:
		some = False
		if sys.argv[i] == '--conf' or sys.argv[i] == '-c':
			some = True
			i+=1
			conf = sys.argv[i]
			i+=1
		elif sys.argv[i] == "--clear" or sys.argv[i] == "-C":
			some = True
			clear = True
			i+=1
		elif sys.argv[i] == "--gui" or sys.argv[i] == "-G":
			some = True
			gui = True
			i+=1
	if not some:
		usage()                        

#main 

manageFlag()

if gui:
	g = Gui()
elif conf != "":
	ce = CompilationEngine(conf)
	m = Manipulator(conf)
	if clear:
		ce.clear()
	else:
		m.generateSource()
		ce.createExes()
		complist = ce.getReport()
		vt = VirusTotal()
		report = vt.getScore(complist)
		print(complist)
		print(report)
else:
	usage()