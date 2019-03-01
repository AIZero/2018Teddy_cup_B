#coding=utf-8
"""
Created on 2018年3月17日
python的版本是3.6
本爬虫主要是通过豆瓣的年份标签获取都有那些电影及url并存储。本爬虫用到了BeautifulSoup这个包，必须先引入这个包。
这个类主要是先调用startSpiderHtml，从豆瓣http://www.douban.com/tag/爱情/movie?start=0·类似网页下载下来，
接下来调用startSpiderMovie，分析之前下载html文件，将其中的电影名字及url提取出来并保存到文本中。
"""
from bs4 import BeautifulSoup
import urllib.request;
import urllib.error;
import string;
import socket
import time;
from email._header_value_parser import Header
import os
class Spider:
    def getHtml(self,url):#从url网站上获取html
        try:
            page=urllib.request.urlopen(url,timeout=10)
            html=page.read()
        except urllib.error.HTTPError:
            return False
        except socket.timeout:
            html=Spider().getHtml(url)
        return html
    def saveHtml(self,html,filename):#将html保存到filename
        fb=open(filename,"wb")
        fb.write(html)
    def saveMovieUrl(self,html,i):#将html页面中的电影及url提取并保存起来
        soup=BeautifulSoup(html,"html.parser")
        for str in soup.find_all('dl')  :
            if str==None:
                return Flase
            str=str.dd
            print(str.a['href'])#电影名字
            file=open(wenjian[i],'a',encoding="UTF-8")
            file.write(str.a['href'])
            file.write('\n')
            print(str.a.string)#电影url
            file.write(str.a.string,)
            file.write('\n')
        return True
    def startSpiderHtml(self,dict,start,end_dict,end_start):#爬取网页,从year年start页开始，到end_year年end_start结束
        """
        由于是从豆瓣标签年份标签爬取的数据，url格式是http://www.douban.com/tag/year/movie?start=start
        里面的dict和start就是我们需要设置的。这个函数将存放电影目录的网页抓取下来。
        """
        dict=dict
        start=start
        i = 0
        proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        while (i<end_dict or start<end_start):
            url="http://www.douban.com/tag/"+str(dict[i])+"/movie?start="+str(start)
            html=Spider.getHtml(Spider(),url)
            soup=BeautifulSoup(html,"html.parser")
            if soup.dl==None:
                print(str(leixing[i])+"已经结束了~")
                i+=1
                start=0
                time.sleep(120)
                continue
            else :
                Spider.saveHtml(Spider(),html,"...\电影/"+str(leixing[i])+"_"+str(start)+".html")
                print(str(leixing[i])+"_"+str(start)+".html已经下载")
            start+=15
            if start%1200==0:
                time.sleep(120)
    def startSpiderMovie(self,i,start,*end):#开始爬取网页中的数据，year是开始年份，start是开始页数
        """
        将startSpiderHtml中获取的html网页解析，从中取出电影名字和具体的url信息，存入文本中。
        """
        i=0
        start=0
        while i<11:
            filename="...\电影/"+str(leixing[i])+"_"+str(start)+".html"
            if(os.path.exists(filename)):
                Spider.saveMovieUrl(Spider(),open(filename,'r',encoding="UTF-8").read(),i)
                start+=15
            else:
                print("~")
                i+=1
                start=0

#Spider().saveHtml(Spider().getHtml("http://movie.douban.com/subject/25835474/?from=showing"),"./test.html")
dict=['%E7%88%B1%E6%83%85','%E7%BB%8F%E5%85%B8','%E5%8A%A8%E4%BD%9C','%E5%96%9C%E5%89%A7','%E6%81%90%E6%80%96','%E7%A7%91%E5%B9%BB',
      '%E6%B2%BB%E6%84%88','%E6%96%87%E8%89%BA','%E6%88%90%E9%95%BF','%E5%8A%A8%E7%94%BB','%E6%82%AC%E7%96%91','2017']
leixing=['爱情','经典','动作','喜剧','恐怖','科幻','治愈','文艺','成长','动画','悬疑']
wenjian=['.../爱情.txt','.../经典.txt','.../动作.txt','.../喜剧.txt','.../恐怖.txt','.../科幻.txt','.../治愈.txt',
         '.../文艺.txt','.../成长.txt','.../动画.txt','.../悬疑.txt']
Spider().startSpiderHtml(dict,0,11,0)
Spider().startSpiderMovie(0, 0)