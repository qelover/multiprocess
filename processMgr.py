import multiprocessing as mProcess


class CProcessMgr:
    def __init__(self, processNum, worker):
        self.processNum = processNum
        self.processList = []
        if not worker:
            return False
        self.worker = worker
    
    
    def produceProcess(self, argsProducer, queue, cBlMgr):
        for i in xrange(self.processNum):
            process = mProcess.Process(target=self.worker.process, args=(argsProducer, queue, cBlMgr) )
            self.processList.append(process)
            
    def startAll(self):
        for pro in self.processList:
            pro.start()
            
    def stopAll(self):
        for pro in self.processList:
            pro.join()
        
