from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
base_url = "http://www.topeduol.com"
html = urlopen(base_url).read().decode("utf-8")
soup = BeautifulSoup(html,"lxml")
all_span = soup.find_all("span",{"class":re.compile(r"atit$")})
num = 0
for i in all_span:
    num = num + 1
    print(i.string)
print(num)


print("-------------------------------------------")

all_teacher = soup.find_all("div",{"class":"a2"})
for teacher in all_teacher :
    print(teacher.string)


print("-------------------------------------------")

all_message = soup.find_all("div",{"class":"link-item-t"})
for message in all_message[0].find_all("a"):
    print(message.string)