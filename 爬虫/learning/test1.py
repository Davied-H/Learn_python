from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re
base_url = "https://www.rijutv.com/dongman/12902.html"
html = urlopen(base_url).read().decode("utf-8")


#通过class筛选标签
# soup = BeautifulSoup(html,"lxml")
# all_a = soup.find_all("a",{"class":"hjtvui-btn hjtvui-btn-radius","href":re.compile(r"html$")})
# print(all_a[0]["href"])

#获取https类型链接时易出现错误，需使用以下方法
# headers = {"Uers-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 YaBrowser/19.3.0.2485 Yowser/2.5 Safari/537.36"}
# rqt = Request("https://tt.fuli.in/6fdcc1ca776/5132/001/002.jpg",headers=headers)
# html = urlopen(rqt)
