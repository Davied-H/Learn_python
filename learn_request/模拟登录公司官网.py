import requests
from bs4 import BeautifulSoup

#模拟使用cookie登录获取操作

conn = requests.session()
url = "http://www.topeduol.com"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
          "Cookie":"PHPSESSID=d03ecc4854744b977a65ece8f15e886d; REMEMBERME=VG9weGlhXFNlcnZpY2VcVXNlclxDdXJyZW50VXNlcjpNVE13TlRFMk56RTNNamxBTVRZekxtTnZiUT09OjE1ODMyMTg0MzY6ODIyOGIzNDQ0MGI3ZWU0YWU1ZDI3OWNmYTZlM2Q0ZWQ1ZTdiZGM4ZWU4MWI2MGQyMWJhMzBkODU3YjQyNjQ0NA%3D%3D"}
data = {"_username":"13331190665","_password":"13910846078"}
r = conn.get(url,headers=header) # 设置header，模拟浏览器登录跳过防爬虫机制，添加cookie登录
html = r.text # 获取text信息（html）

#使用bs4 解析网页
soup = BeautifulSoup(html,"lxml")
user_menu = soup.find_all("ul",{"class":"dropdown-menu my-pag"})
#通过浏览器开发者模式找到用户的个人memu
homepage = user_menu[0].find_all("li")
# print(homepage[1].a["href"])
new_url = url + homepage[1].a["href"] #生成新的url，homepage[1]为用户主页的li
new_r = conn.get(new_url) #此时访问时不用再次提交cookie，因为conn是个持续连接
# print(new_url)
print(new_r.text) #打印新网页