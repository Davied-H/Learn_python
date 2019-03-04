import requests
from bs4 import BeautifulSoup

conn = requests.session()
url = "http://www.topeduol.com/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
          "Cookie":"PHPSESSID=d03ecc4854744b977a65ece8f15e886d; REMEMBERME=VG9weGlhXFNlcnZpY2VcVXNlclxDdXJyZW50VXNlcjpNVE13TlRFMk56RTNNamxBTVRZekxtTnZiUT09OjE1ODMyMTg0MzY6ODIyOGIzNDQ0MGI3ZWU0YWU1ZDI3OWNmYTZlM2Q0ZWQ1ZTdiZGM4ZWU4MWI2MGQyMWJhMzBkODU3YjQyNjQ0NA%3D%3D"}
data = {"_username":"13331190665","_password":"13910846078"}
r = conn.get(url,headers=header)
html = r.text

soup = BeautifulSoup(html,"lxml")
user_menu = soup.find_all("ul",{"class":"dropdown-menu my-pag"})
homepage = user_menu[0].find_all("li")
# print(homepage[1].a["href"])


