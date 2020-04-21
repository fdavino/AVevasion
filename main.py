import sys
from compEngine import CompilationEngine
from virusTotal import VirusTotal

def usage():
    print("usage: python3 createExes.py config.conf.json [--clear|-c]")

#main 

if len(sys.argv) > 1:
    ce = CompilationEngine(sys.argv[1])
else:
    usage()    

if len(sys.argv) > 2:
    if sys.argv[2] == "-c" or sys.argv[2] == "--clear":
        ce.clear()
    else:
        usage()
else:
    ce.createExes()

report = {}
compList = ce.getReport()
for compiled in compList:
    vt = VirusTotal(ce.apikey,compList[compiled])
    report[compiled] = vt.getScore(compList[compiled])

print(report)
     

