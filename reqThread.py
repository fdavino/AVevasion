import threading
import time

req = 0
delay = 0
limit = 4

class ReqThread(threading.Thread):

        scores = []
        lock = threading.Lock()

        def __init__(self, threadID, scan, report, source, scores):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.scan = scan
            self.report = report
            self.source = source
            self.scores = scores

        def __delayup(self, inc):
            global req
            global delay
            global limit
            global thism
            req += inc
            delay = req // limit

        def __getdelay(self):
            try:
                self.lock.acquire()
                global delay
                s = delay*60
                self.__delayup(1)
                self.lock.release()
                return s
            except Exception as e:
                print(e)
                if self.lock.locked():
                    self.lock.release()
                return delay*60
            
    
        def run(self):
            slt = self.__getdelay() #sync

            time.sleep(slt)
            scanid = self.scan(self.source)

            tmp = self.__getdelay() #sync
            slt += tmp #sync

            time.sleep(tmp)
            self.scores[self.threadID] = self.report(scanid)
            
            while self.scores[self.threadID] == (-1,1):
                tmp = self.__getdelay() #sync
                print("Thread {} resource queued, wait".format(self.threadID))
                print("Thread {} sleep {}s and recall".format(self.threadID, tmp - slt))
                time.sleep(tmp - slt) #sync
                slt += tmp - slt #sync
                self.scores[self.threadID] = self.report(scanid)


                                




