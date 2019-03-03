from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
base_url = "https://www.rijutv.com/v_all/list-catid-12-year-2019.html"
html = urlopen(base_url).read().decode("utf-8")

soup = BeautifulSoup(html,"lxml")
all_a = soup.find_all("a",{"href":re.compile(r"^/dongman"),"class":"thumb"})

url = "https://www.rijutv.com"
for i in all_a :
    try:
        new_url = url + i["href"]
        html = urlopen(new_url).read().decode("utf-8")
        soup1 = BeautifulSoup(html, "lxml")
        all_a = soup1.find_all("a", {"class": "hjtvui-btn hjtvui-btn-radius", "href": re.compile(r"html$")})
        print(soup1.h1.string + ":" + url +  all_a[0]["href"] )

    except:
        pass




