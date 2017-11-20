#coding:utf-8
import threading,Queue
from collections import deque
from toolhand import *
import pdb
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
    #pdb.set_trace()
    while True:
        allurl = db.selecturls2()
        if len(allurl) == 0:
            break
        while len(allurl) > 0:
            t = allurl.pop()
            allstar(t,db)
            
    print "stop\n"

if __name__ == "__main__":
    main()
