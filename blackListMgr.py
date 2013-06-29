from multiprocessing import Queue
import queueMgr
import confile as conf


class CBlackListMgr:
  def __init__(self, fileNameList):
		self.cQMgr = queueMgr.CQueueMgr()
		self.queueNum = self.cQMgr.getQueueNum(fileNameList)
		self.queue = Queue(self.queueNum)
		self.initBlackList()


	def setBlackList(self, fileName):
		self.queue.put(fileName)

	"""
	def __getBlackList(self):
		blackList = []
		for i in xrange(self.queue.qsize() ):
			blackList.append(self.queue.get() )

		return blackList
	"""

	def getBlackList(self):
		return self.queue

	def initBlackList(self):
		iFile = open(conf.blackListFileName)
		line = iFile.readline()
		while line:
			#processedFileList.append(line)
			line = line.strip("\n")
			self.queue.put(line)
			line = iFile.readline()
		iFile.close()
		
	def writeBlackList(self):
		blackListFile = open(conf.blackListFileName, "w")
		
		for i in xrange(self.queue.qsize() ):
			blackListFile.write(self.queue.get()+"\n")

		blackListFile.close()
	
