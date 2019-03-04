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
    div_list = teacher.contents #将span标签所以子节点存入list中
    #去除teacher_list 中的"\n"属性
    for div in range(len(div_list)-1,-1,-1): #使用range反序循环，正序容易出现下标越界错误
        if div_list[div] == '\n':
            div_list.remove('\n')
    every_teacher = div_list[2].string
    print(div_list[3])
    print(div_list[3].contents[0].p)
    # print(re.search(r"^<p>*</p>$",div_list[3].a.string))
    # print(teacher.conten1ts)
print("-------------------------------------------")

all_message = soup.find_all("div",{"class":"link-item-t"})
for message in all_message[0].find_all("a"):
    print(message.string)