import sys
from compEngine import CompilationEngine
from virusTotal import VirusTotal
from manipulator import Manipulator


rate = 0.05
sc = ""
payload = ""
conf = ""
clear = False

def usage():
    print("usage: python3 createExes.py")
    print("\t(--conf | -c) configuration file")
    print("\t(--payload | -p) payload file")
    print("\t(--specialchar | -s) special character")
    print("\t[--rate | -r] frequence of special character in payload")
    print("\t[--clear | -C] remove folders of precedent executions")

def manageFlag():
    global rate
    global sc
    global payload
    global conf
    global clear
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '--rate' or sys.argv[i] == '-r':
            i+=1
            try:
                rate = float(sys.argv[i])
            except ValueError:
                print("rate must be decimal\n")
                sys.exit(1)
            i+=1
        elif sys.argv[i] == '--specialchar' or sys.argv[i] == '-s':
            i+=1
            sc = sys.argv[i]
            i+=1
        elif sys.argv[i] == '--payload' or sys.argv[i] == '-p':
            i+=1
            payload = sys.argv[i]
            i+=1
        elif sys.argv[i] == '--conf' or sys.argv[i] == '-c':
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

if clear and ce != None:
    ce.clear()
elif sc != "" and payload != "":
    m = Manipulator(sc, rate)
    m.generateSource()
    ce.createExes()
    complist = ce.getReport()
    vt = VirusTotal()
    report = vt.getScore(complist)

    print(complist)
    print(report)
else:
    usage()