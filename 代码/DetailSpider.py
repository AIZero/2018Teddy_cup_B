#coding=utf-8
from Spider import Spider
from bs4 import BeautifulSoup
import urllib.request
import re
from _codecs import encode
import time
import threading
class DetailSpider:
    '''
  Created on 2018年3月17日
  python的版本是3.6
    首先调用getMovieHtml，将Spider中抓取的电影名字及url提取出来，并将url指向的网页抓取下来，
    接下来调用getMovieDetail将分析和提取使用getMovieHtml抓取的html页面，这个提取的信息就是影片的具体信息，保存到文本文件中
    '''


    def getMovieHtml(self,filename,name,j,end,z):#从filename中获取影片存放影片具体信息的网页url，抓取url指向的网页，name是开始url，抓取下来保存文件的名字，end是结束url
        file=open(filename,'r',encoding="UTF-8")
        i=0
        j=j
        flag=False
        for url in file:
            if i%2==0:
                m=re.search(r'h.*', url)
                if m.group()==name:
                    flag=True
                if flag:
                    html=Spider().getHtml(m.group())
                    if html:
                        Spider().saveHtml(html, dizhi[z]+str(j)+".html")
                        print(str(m)+" :"+str(j)+".html已存储~")
                        j+=1
                if m.group()==end:
                    return
            else:
                print(url.strip())
            i+=1
        if j%90==0 :
            time.sleep(120)#为了防止请求过于频繁，抓取一定页数就暂停一下
    def getMovieDetail(self,filename,i):#分析网页，获取网页中的数据，存入文本中
        file=open(filename,'r',encoding="UTF-8")
        html=file.read()
        soup=BeautifulSoup(html,"html.parser")
        if not soup.find("div",id='content'):
            return
        soup=soup.find("div",id='content')
        if not soup.find('span',property="v:itemreviewed"):
            return
        print(soup.find('span',property="v:itemreviewed").string)
        dict={'name':soup.find('span',property="v:itemreviewed").string}
        dict['name']=soup.find('span',property="v:itemreviewed").string#电影名称

        info=soup.find(id='info')
        s="{"
        #print(info.getText().replace(": ",":"))
        line = info.getText().replace(": ",":").replace(":\n",":").split("\n")[4]
        line=line.replace("'","")
        if line !='':
            #print(line.split(":",1))
            s+="'"+line.split(":",1)[0]+"'"+":"+"'"+line.split(":",1)[1]+"',"
        s=s[:-1]+"}"
        #print(s)
        dict.update(eval(s))

        dict['summary'] = soup.find(id="link-report").getText().replace("\n", "").replace("\u3000", "").replace(
            "                                ", "").replace("                        ", "")
        #print(dict)

        file=open(cunfang[i],"a",encoding="UTF-8")
        file.write(str(dict))
        file.write("\n")
        file.close()

filename=['.../爱情.txt','.../经典.txt','.../动作.txt','.../喜剧.txt','.../恐怖.txt','.../科幻.txt','.../治愈.txt',
         '.../文艺.txt','.../成长.txt','.../动画.txt','.../悬疑.txt']
name=['https://movie.douban.com/subject/26799731/?from=tag_all','https://movie.douban.com/subject/26607693/?from=tag_all',
      'https://movie.douban.com/subject/26607693/?from=tag_all','https://movie.douban.com/subject/26588314/?from=tag_all',
      'https://movie.douban.com/subject/3604148/?from=tag_all','https://movie.douban.com/subject/10512661/?from=tag_all',
      'https://movie.douban.com/subject/26654146/?from=tag_all','https://movie.douban.com/subject/26799731/?from=tag_all',
      'https://movie.douban.com/subject/26799731/?from=tag_all','https://movie.douban.com/subject/20495023/?from=tag_all',
      'https://movie.douban.com/subject/26607693/?from=tag_all']
dizhi=['...\豆瓣电影\爱情/','...\豆瓣电影\经典/','...\豆瓣电影\动作/','...\豆瓣电影\喜剧/','...\豆瓣电影\恐怖/','...\豆瓣电影\科幻/',
       '...\豆瓣电影\治愈/','...\豆瓣电影\文艺/','...\豆瓣电影\成长/','...\豆瓣电影\动画/','...\豆瓣电影\悬疑/']
cunfang=['...\豆瓣电影\存放/爱情.txt','...\豆瓣电影\存放/经典.txt','...\豆瓣电影\存放/动作.txt','...\豆瓣电影\存放/喜剧.txt',
         '...\豆瓣电影\存放/恐怖.txt','...\豆瓣电影\存放/科幻.txt','...\豆瓣电影\存放/治愈.txt','...\豆瓣电影\存放/文艺.txt',
         '...\豆瓣电影\存放/成长.txt', '...\豆瓣电影\存放/动画.txt','...\豆瓣电影\存放/悬疑.txt']
#从豆瓣上抓取html页面
for i in range(0,11):
    DetailSpider().getMovieHtml(filename[i],name[i], 0, 2706,i)

for i in range(0,11):
    if i == 0:
        start = 0
        while start < 300:
            print("start=" + str(start))
            filename = dizhi[i] + str(start) + ".html"
            DetailSpider().getMovieDetail(filename, i)
            start += 1
    if i == 1:
        start = 0
        while start < 296:
            print("start=" + str(start))
            filename = dizhi[i] + str(start) + ".html"
            DetailSpider().getMovieDetail(filename, i)
            start += 1
    if i == 2:
        start = 0
        while start < 295:
            print("start=" + str(start))
            filename = dizhi[i] + str(start) + ".html"
            DetailSpider().getMovieDetail(filename, i)
            start += 1
    if i == 3:
        start = 0
        while start < 299:
            print("start=" + str(start))
            filename = dizhi[i] + str(start) + ".html"
            DetailSpider().getMovieDetail(filename, i)
            start += 1
    if i == 4:
        start = 0
        while start < 277:
            print("start=" + str(start))
            filename = dizhi[i] + str(start) + ".html"
            DetailSpider().getMovieDetail(filename, i)
            start += 1
    if i == 5:
        start = 0
        while start < 299:
            print("start=" + str(start))
            filename = dizhi[i] + str(start) + ".html"
            DetailSpider().getMovieDetail(filename, i)
            start += 1
    if i == 6:
        start = 0
        while start < 300:
            print("start=" + str(start))
            filename = dizhi[i] + str(start) + ".html"
            DetailSpider().getMovieDetail(filename, i)
            start += 1
    if i == 7:
        start = 0
        while start < 298:
            print("start=" + str(start))
            filename = dizhi[i] + str(start) + ".html"
            DetailSpider().getMovieDetail(filename, i)
            start += 1
    if i == 8:
        start = 0
        while start < 299:
            print("start=" + str(start))
            filename = dizhi[i] + str(start) + ".html"
            DetailSpider().getMovieDetail(filename, i)
            start += 1
    if i == 9:
        start = 0
        while start < 296:
            print("start=" + str(start))
            filename = dizhi[i] + str(start) + ".html"
            DetailSpider().getMovieDetail(filename, i)
            start += 1


