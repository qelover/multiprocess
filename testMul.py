import processMgr as proMgr
import fileDispatcher as fileDisp
import workerInterface as workInter
import fileUtil as fUtil
import confile as conf
import queueMgr
import blackListMgr as blMgr


class CTestMul:
    def __init__(self, worker, argsProducer, filePath):
        self.worker = worker
        self.argsProducer = argsProducer
        self.filePath = filePath
        self.fileNameList = None
        
    
    def getProcessNum(self):
        self.fileNameList = []
        fUtil.getFileNameList(self.fileNameList, self.filePath)
        
        fileNum = len(self.fileNameList)
        processNum = conf.processNum
        if fileNum < processNum:
            processNum = fileNum
   
        return processNum
    
    def pipeline(self):
        processNum = self.getProcessNum()
        print processNum
        processMgr = proMgr.CProcessMgr(processNum, self.worker)

        cQueue = queueMgr.CQueueMgr()
        cBlMgr = blMgr.CBlackListMgr(self.fileNameList)
        queue = cQueue.getQueueUsingBlackList(cBlMgr, self.fileNameList)
        processMgr.produceProcess(self.argsProducer, queue, cBlMgr)

        processMgr.startAll()
        processMgr.stopAll()

        cBlMgr.writeBlackList()

if __name__ == "__main__":
    worker = workInter.CAutoNavOffline()
    argsProducer = fileDisp.CFileDispatcher()
    filePath = "/apsarapangu/disk1/wei.qin/Data/inputHistory"
    
    cTestMul = CTestMul(worker, argsProducer, filePath)
    cTestMul.pipeline()
    
