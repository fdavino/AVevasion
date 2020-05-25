import sys
sys.path.append("Component")
sys.path.append("Driver")
from compEngine import CompilationEngine
from virusTotal import VirusTotal
from manipulator import Manipulator


conf = ""
clear = False

def usage():
    print("usage: python3 main.py")
    print("\t(--conf | -c) configuration file")
    print("\t[--clear | -C] remove folders of precedent executions")
    sys.exit(1)

def manageFlag():
    global conf
    global clear
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '--conf' or sys.argv[i] == '-c':
            i+=1
            conf = sys.argv[i]
            i+=1
        elif sys.argv[i] == "--clear" or sys.argv[i] == "-C":
            clear = True
            i+=1            

#main 

manageFlag()

if conf != "":
    ce = CompilationEngine(conf)
    m = Manipulator(conf)
else:
    usage()    

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