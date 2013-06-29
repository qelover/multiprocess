import sys
sys.path.append("../")
import autoNavOffline as autonav


class CWorkerInterface(object):
    def __init__(self):
        print "__init__ fun() in workerInterface"
    
    def process(self):
        print "process fun() in workerInterface"
        
        
class CWorkerTest(CWorkerInterface):
    def __init__(self):
        super(CWorkerTest, self).__init__()
        
    def process(self, args):
        print args
    

class CAutoNavOffline(CWorkerInterface):
    def __init__(self):
        pass
    
    def process(self, argsProducer, queue, cBlMgr):
        cReader = autonav.CGetDataFromLogReader()
        cReader.process(argsProducer, queue, cBlMgr)
        

