import json
import subprocess
import os
import sys
import shutil

def usage():
    print("usage: python3 createExes.py config.conf.json [--clear|-c]")

def createPath(info):
    path = "{}/{}".format(info['path'],info['filename'])
    return path

#execute a list of compilations
def createExes(): 
#parse config file
    with open(CONF_FILE) as json_conf:
        data = json.load(json_conf)
        info = data['info']
        compilers = dict(data['compilers'])
#create command string
    for c in compilers:
        field = dict(compilers[c])

        f = createPath(info)

        command = field['path']
        for o in field['optionBefore']:
            command = "{} {}".format(command,o)
        command = "{} {}".format(command,f)
        for o in field['optionAfter']:
            command = "{} {}".format(command,o)

#create destionation folder
        if(not(os.path.exists(c)) or not(os.path.isdir(c))):
            os.mkdir(c)
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

if(len(sys.argv) > 1):
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

    
        
            

