import ssl
from urllib.request import urlopen,Request
context = ssl._create_unverified_context


#获取https类型链接时易出现错误，需使用以下方法
headers = {"Uers-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 YaBrowser/19.3.0.2485 Yowser/2.5 Safari/537.36"}
rqt = Request("https://tt.fuli.in/6fdcc1ca776/5132/001/002.jpg",headers=headers)
html = urlopen(rqt)