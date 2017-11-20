
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Queue
import threading
import time
from toolhand import *
 
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name
 
def process_data(threadName, q):
    while True:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            #self.tmp.append(info)
            db = dbhand(self.logger)
            dbfile = "todayb.db"
            db.dbconnect(dbfile)
            db.initdatabase()#数据表初始化
            #for tt in self.tmp:
            allstar(tt,db)
            #self.tmp = []
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
 
threadList = ["Thread-1","thread-2","thread-3","thread-4","thread-5"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue()
threads = []
threadID = 1
 
# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
start = {}
start['url'] = "http://www.sxyyc.net"
logop = {}
logop['logfile'] = "log.txt"#uop['logfile']
logop['loglevel'] = "INFO"#uop['level']
global logger
logger = getlog(logop)#构造log对象
global db
db = dbhand(logger)
dbfile = "todayb.db"
db.dbconnect(dbfile)
db.initdatabase()#数据表初始化
db.selecturls2()
db.insertone(start,'urls')

# 填充队列
queueLock.acquire()
urls = db.selecturls2()
for word in urls:
    workQueue.put(word)
    workQueue.join()
queueLock.release() 
print "Exiting Main Thread"
