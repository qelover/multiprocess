import multiprocessing as mProcess


class CFileDispatcher:
    def __init__(self):
        self.lock = mProcess.Lock()
    
    def getOneFile(self, queue):
        self.lock.acquire()
        if queue.empty() > 0:
            fileName = None
        else:
            fileName = queue.get()
        self.lock.release()
        
        return fileName
    
    def getArgs(self, queue):
        return self.getOneFile(queue)
