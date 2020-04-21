import json
import subprocess
import os
import sys
import shutil

class CompilationEngine:
    
    conf_file = ""
    apikey = ""

    def __init__(self, conf_file):
        self.conf_file = conf_file
        self.outlist = {}

#execute a list of compilations
    def createExes(self): 
#parse config file
        with open(self.conf_file) as json_conf:
            data = json.load(json_conf)
            info = dict(data['info'])
            if not "inputFile" in info or not "apikey" in info:
                print("ERROR: input file not specified")
                sys.exit(1) 
            self.apikey = info['apikey']
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
                command = self.__addOptions(command, options1)
        
            command = "{} {}".format(command,info["inputFile"])
    
            if "options2" in cInExam:
                options2 = cInExam['options2']
                command = self.__addOptions(command, options2)
        
#create destionation folder
            if(not(os.path.exists(c)) or not(os.path.isdir(c))):
                os.mkdir(c)
#redirect on log file
            command = "{} 2>&1 > error-{}.log".format(command, c)
#compiling
            os.chdir(c)
            print("... Executing {}".format(command))
            subprocess.call(command,shell=True)
            self.__addToReport(c)
            os.chdir("..")
            print("End {}".format(c))

#remove all dir and file created by an execution
    def clear(self): 
        with open(self.conf_file) as json_conf:
            data = json.load(json_conf)
            info = data['info']
            compilers = dict(data['compilers'])
        print("...Clearing")
        for c in compilers:
            if(os.path.exists(c) and os.path.isdir(c)):
                shutil.rmtree(c,True)
        print("Done")


    def getReport(self):
        return self.outlist


    def __addOptions(self, command, options):
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

    def __addToReport(self, comp):
        output = [f for f in os.listdir('.'.format(comp)) if not f.endswith(".log")]
        self.outlist[comp] = "./{}/{}".format(comp,output[0])        



    
        
            

