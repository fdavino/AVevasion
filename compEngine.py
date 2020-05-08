import json
import subprocess
import os
import sys
import shutil

class CompilationEngine:
    
    conf_file = ""

    def __init__(self, conf_file):
        self.conf_file = conf_file
        self.outlist = {}

    def __checkObF(self, field, container):
        if not field in container:
        	raise KeyError("{} is an obligatory field".format(field))

#execute a list of compilations
    def createExes(self): 
#parse config file
        with open(self.conf_file) as json_conf:
            data = json.load(json_conf)
            self.__checkObF("compilers", data)
            compilers = data['compilers']
            self.__checkObF("manipulations",data)
            manipulations = data['manipulations']
            out = "out.c"
            if "out" in manipulations:
            	out = manipulations['out']

#create command string
        if os.path.exists(out):
            for c in compilers:
                cInExam = compilers[c]
                self.__checkObF("path", cInExam)
                command = "{} ".format(cInExam["path"])
    
                if "options1" in cInExam:
                    options1 = cInExam['options1']
                    command = self.__addOptions(command, options1)   

                command = "{} {}".format(command,os.path.abspath(out))
    
                if "options2" in cInExam:
                    options2 = cInExam['options2']
                    command = self.__addOptions(command, options2)

#create destionation folder
                if(not(os.path.exists(c)) or not(os.path.isdir(c))):
                    os.mkdir(c)
#redirect on log file
                command = "{} > error-{}.log 2>&1".format(command, c)
#compiling
                os.chdir(c)
                print("... Executing {}".format(command))
                subprocess.call(command,shell=True)
                self.__addToReport(c)
                os.chdir("..")
                print("End {}".format(c))
        else:
        	raise FileNotFoundError("{} not generated".format(out))
      

#remove all dir and file created by an execution
    def clear(self): 
        with open(self.conf_file) as json_conf:
            data = json.load(json_conf)
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
                self.__checkObF("name",olist)
                command = "{} {}".format(command,olist['name'])
                
                if "value" in olist:
                    for val in olist['value']:
                        command = "{} {}".format(command,val)
        return command

    def __addToReport(self, comp):
        output = [f for f in os.listdir('.'.format(comp)) if not f.endswith(".log")]
        if len(output) != 0:
            self.outlist[comp] = os.path.abspath(output[0])