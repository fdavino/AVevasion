import requests
import json
import os
import sys
import numpy as np
from compEvaluator import CompEvaluator
from reqThread import ReqThread


class VirusTotal(CompEvaluator):

    apikey = ""   

    def __init__(self):
        
        if(not os.path.exists("vtkey.json")):
            print("vtkey.json \n { \"apikey\": \"APIKEY_VALUE\" } format \n needed")
            sys.exit(1)
        with open("vtkey.json") as key:
            data = json.load(key)
            if 'apikey' not in data:
                print("vtkey.json \n { \"apikey\": \"APIKEY_VALUE\" } format \n needed")
                sys.exit(1)
            self.apikey = data['apikey'] 

#upload the file to virustotal, return scan_id
    def __scan(self,source):
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': '{}'.format(self.apikey)}
        files = {'file': ('{}'.format(source), open(source, 'rb'))}
        response = requests.post(url, files=files, params=params)
        if response.status_code == 200:
            res = response.json()
            return res['scan_id']
        else:
            print("Response Code :{}".format(response.status_code))
            return -1
        
#lookup stats of file defined by scanid, return (positive,total)
    def __report(self,scanid):
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': '{}'.format(self.apikey), 'resource': '{}'.format(scanid)}
        if scanid != -1:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                res = response.json()
            
                if 'positives' in res:
                    positive = res['positives']
                    total = res['total']
                    return (positive,total)
                else:
                    return (-1,1)               
            else:
                print("Response Code :{}".format(response.status_code))
                return (-2,1)
        else:
            return (-2,1)
            
    def getScore(self, sources):
        l = (1 if isinstance(sources, str) else len(sources)) 
        scores = np.empty(l, dtype=tuple) 
        threads = np.empty(l, dtype=object)
        i = 0
        for f in sources:
            threads[i] = ReqThread(i, self.__scan, self.__report, sources[f], scores)
            threads[i].start()
            i=i+1
        for t in threads:
            t.join()
        
        return scores

    
            
        
        



    

    
