import requests
from urllib.request import urlopen
from bs4  import BeautifulSoup
import webbrowser # 用来调用系统默认浏览器打开网页，webbrowser.open(url)
import  sys

#get 方式
# params = sys.argv[1]
params = "qq"
base_url = "http://www.baidu.com/s"
r = requests.get(url=base_url,params=params)
# print(r.text) //获取网页 同 urllib.request.urlopen
# print(r.headers) //获取响应头
# print(r.request) //获取数据提交方式

#post 方式





