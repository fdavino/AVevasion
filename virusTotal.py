import requests
import json

class VirusTotal:
    
    apikey = ""
    
    def __init__(self, apikey, source):
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
            positive = res['positives']
            total = res['total']
        else:
            positive = -1
            total = 1
        
        return (positive,total)

#return the score of the source
    def getScore(self,source):
        scanid = self.__scan(source)
        score = self.__report(scanid)
      
        return score[0]/ score[1]
        



    

    
