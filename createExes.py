import json
import subprocess
import os
import sys
import shutil

def usage():
    print("usage: python3 createExes.py config.conf.json [--clear|-c]")

def createPath(info):
    path = info['path']
    return path

def addOptions(command, options):
    for olist in options:
                if "name" in olist:
                    command = "{} {}".format(command,olist['name'])
                else:
                    print("ERROR: every option need a name")
                    continue
                if "value" in olist:
                    for val in olist['value']:
                        command = "{} {}".format(command,val)
    return command

#execute a list of compilations
def createExes(): 
#parse config file
    with open(CONF_FILE) as json_conf:
        data = json.load(json_conf)
        info = dict(data['info'])
        if not "inputFile" in info:
            print("ERROR: input file not specified")
            sys.exit(1) 
        compilers = dict(data['compilers'])

#create command string
    for c in compilers:
        cInExam = compilers[c]
        if "path" in cInExam:
            command = "{} ".format(cInExam["path"])
        else:
            print("ERROR: {} not have a path".format(c))
            continue

        if "options1" in cInExam:
            options1 = cInExam['options1']
            command = addOptions(command, options1)
        
        command = "{} {}".format(command,info["inputFile"])

        if "options2" in cInExam:
            options2 = cInExam['options2']
            command = addOptions(command, options2)
        
        print(command)
#create destionation folder
        if(not(os.path.exists(c)) or not(os.path.isdir(c))):
            os.mkdir(c)
#redirect on log file
        command = "{} 2>&1 > error-{}.log".format(command, c)
#compiling
        os.chdir(c)
        print("... Executing {}".format(command))
        subprocess.call(command,shell=True)
        os.chdir("..")
        print("End {}".format(c))

#remove all dir and file created by an execution
def clear(): 
    with open(CONF_FILE) as json_conf:
        data = json.load(json_conf)
        info = data['info']
        compilers = dict(data['compilers'])
    print("...Clearing")
    for c in compilers:
        if(os.path.exists(c) and os.path.isdir(c)):
            shutil.rmtree(c,True)
    print("Done")


#main 

if len(sys.argv) > 1:
    CONF_FILE = sys.argv[1]
else:
    usage()    

if len(sys.argv) > 2:
    if sys.argv[2] == "-c" or sys.argv[2] == "--clear":
        clear()
    else:
        usage()
else:
    createExes()

    
        
            

