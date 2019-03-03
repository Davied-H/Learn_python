from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
base_url = "https://www.rijutv.com/dongman/12902.html"
html = urlopen(base_url).read().decode("utf-8")

soup = BeautifulSoup(html,"lxml")
all_a = soup.find_all("a",{"class":"hjtvui-btn hjtvui-btn-radius","href":re.compile(r"html$")})
print(all_a[0]["href"])


