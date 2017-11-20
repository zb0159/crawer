import urllib.request
from bs4 import BeautifulSoup
import os,sys
#解析
def crawerEach(url,urldir):
    resp=urllib.request.urlopen(url)
    html=resp.read().decode('gbk')
    soup = BeautifulSoup(html)
    
#中文转为网页url编码格式
def wordstoutf(words):
    value=urllib.request.quote(words)
    return value

#把内容写入文件
def writeContent(content):
    f=open('content1.txt','a',encoding='utf-8')
    f.write(content)
    f.close()

#读文件，一行一行读
def readfile(filename):
    f=open(filename,'r')
    res = f.readlines()
    for r in res:
        content=soupctl(r)
        wrc = "%s-%s\n" % (r.strip("\n"),content)
        writeContent(wrc)
        print ("finded"+str(r.strip('\n'))+str(content))
    f.close()
#根据学校名称查找学校网址，并返回
def soupctl(univer):
    words = univer
    url ="http://www.baidu.com/s?wd="+str(wordstoutf(words))
    print ("start\n")
    data = ""
    try:
        data = urllib.request.urlopen(url,timeout=10).read()
    except:
        return "no" 
    print ("end\n")
    html = data.decode('UTF-8')
    soup = BeautifulSoup(html,"html.parser")
    try:
        contents = soup.find('body').find('div',id='1').find(name='div',attrs={"class":"f13"}).find('a').string
        print ("1="+contents)
    except:
        try:
            contents = soup.find('body').find('div',id='2').find(name='div',attrs={"class":"f13"}).find('a').string
            print("2="+contents)
        except:   
                    
                return "no"
    return contents
#根据一个网址，获取该网页下的所有超链接地址
def get_all_link_from_page(url):
    data = urllib.request.urlopen(url).read()
    html = data.decode('UTF-8')
    soup = BeautifulSoup(html,"html.paraser")

    try:
        links = soup.find('body').find_all('a').string
        print (links)
    except:
        print ("soup erro\n")




#定义主函数
def main():
    #try:
    readfile("lib_benke.txt")
#        get_all_link_from_page("http://www.sxyyc.net/")
    #except:
    #    return
#运行主函数
main()
