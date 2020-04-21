import requests
import json
import threading
import numpy as np

class ReqThread(threading.Thread):

    scores = []

    def __init__(self, threadID, function, source, scores):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.function = function
        self.source = source
        self.scores = scores
    
    def run(self):
        self.scores[self.threadID] = self.function(self.source)

class VirusTotal:
    
    apikey = ""
    lock = threading.Lock()   

    def __init__(self, apikey):
        self.apikey = apikey

#upload the file to virustotal, return scan_id
    def __scan(self,source):
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': '{}'.format(self.apikey)}
        files = {'file': ('{}'.format(source), open(source, 'rb'))}
        response = requests.post(url, files=files, params=params)
        res = response.json()
        return res['scan_id']
        
#lookup stats of file defined by scanid, return (positive,total)
    def __report(self,scanid):
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': '{}'.format(self.apikey), 'resource': '{}'.format(scanid)}
        
        response = requests.get(url, params=params)
        print("VirusTotal API response code : {}".format(response.status_code))
        if response.status_code == 200:
            res = response.json()
            
            if 'positives' in res:
                positive = res['positives']
                total = res['total']
                print("{}/{}".format(positive,total))
                return (positive,total)
            else:
                print("Resource queued")
                return (-1,1)                
        else:
            return (-1,1)
            

#return the score of the source
    def getScore(self,source):
        try:
            self.lock.acquire()
            scanid = self.__scan(source)
            score = self.__report(scanid)
            self.lock.release()
            return score[0]/ score[1]
        except Exception as e:
            print(e)
            self.lock.release()
            return -1    
        

    def multithread_getScore(self, sources):
         
        scores = np.empty(len(sources), dtype=float) 
        threads = np.empty(len(sources), dtype=object)
        i = 0
        for f in sources:
            threads[i] = ReqThread(i, self.getScore, sources[f], scores)
            threads[i].start()
            i=i+1
        for t in threads:
            t.join()
        
        return scores
            
        
        



    

    
