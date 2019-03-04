from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
base_url = "http://www.topeduol.com" #url
html = urlopen(base_url).read().decode("utf-8") #使用urlopen函数访问网页并获取html页面
soup = BeautifulSoup(html,"lxml") #使用bs4实例化
all_span = soup.find_all("span",{"class":re.compile(r"atit$")})
num = 0
for i in all_span:
    num = num + 1
    print(i.string)
print(num)


print("-------------------------------------------")

all_teacher = soup.find_all("div",{"class":"pic",})
for teacher in all_teacher :
    teacher_name = teacher.find_all("div",{"class":"a2"})[0].string
    teacher_message = teacher.p.get_text()
    print(teacher_name + "\n" + teacher_message)
print("-------------------------------------------")

all_message = soup.find_all("div",{"class":"link-item-t"})
for message in all_message[0].find_all("a"):
    print(message.string)