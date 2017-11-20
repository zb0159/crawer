#coding:utf-8
import threading,Queue
from collections import deque
from toolhand import *
import pdb
class multigeturl(threading.Thread):
    '''线程'''
    global temp
    def __init__(self,queue,threadname,logger,lock):
        threading.Thread.__init__(self,name=threadname)
        self.queue = queue
        self.lock = lock
        self.logger = logger
        self.tmp = []
    def run(self):
        print "start "+self.getName()  
        while True:
            self.lock.acquire()
            info = self.queue.get()
            self.tmp.append(info)
            db = dbhand(self.logger)
            dbfile = "todayb.db"
            db.dbconnect(dbfile)
            db.initdatabase()#数据表初始化
            for tt in self.tmp:
                print tt
                allstar(tt,db)
            self.tmp = []
            self.lock.release()
            self.queue.task_done()

        print "exit "+self.getName()
def main():
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
    db.insertone(start,'urls')
    queue = Queue()
    threadnumber =10 
    allurl = db.selecturls2()
    lock = threading.Lock()
    for i in range(threadnumber):#初始化线程池
        t1 = multigeturl(queue,'urlt_'+str(i),logger,lock)
        t1.setDaemon(True)
        t1.start()

    while True:
        while len(allurl) > 0:
            t = allurl.pop()
            queue.put(t)
            print "main queue add"+str(t) 
        queue.join()
        allurl = db.selecturls2()

if __name__ == "__main__":
    main()
