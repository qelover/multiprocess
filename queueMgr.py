from multiprocessing import Queue
import blackListMgr as blMgr


class CQueueMgr:
    def __init__(self):
        pass
    
    def getQueueNum(self, fileNameList):
        return len(fileNameList)
    
    def getQueue(self, fileNameList):
        queueNum = self.getQueueNum(fileNameList)
        fileQueue = Queue(queueNum)
        for i in xrange(queueNum):
            fileQueue.put(fileNameList[i])
        return fileQueue
 
    def getQueueUsingBlackList(self, cBlMgr, fileNameList):
        blQueue = cBlMgr.getBlackList()
        blList = []
        for i in xrange(blQueue.qsize() ):
            fileName = blQueue.get()
            blList.append(fileName)
            if fileName in fileNameList:
                fileNameList.remove(fileName)

        for i in xrange(len(blList) ):
            cBlMgr.setBlackList(blList[i])

        return self.getQueue(fileNameList)

