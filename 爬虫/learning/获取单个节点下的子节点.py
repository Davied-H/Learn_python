from bs4 import BeautifulSoup
from urllib.request import urlopen
import  re


base_url = "http://www.topeduol.com"
html = urlopen(base_url).read().decode("utf-8")
# print(html)

soup = BeautifulSoup(html,"lxml")
# print(type(soup)) //bs4.BeautifulSoup

#获取class=pic的div
all_div = soup.find_all("div",{"class":"pic"})
# print(type(all_div)) //bs4.element.ResultSet

#循环遍历，获取每个大的div_tag
for teacher_div in all_div :
    # print(teacher_div.p) //可对tag类型直接使用标签方法
    teacher_message = teacher_div.p
    print(type(teacher_message))
    print(teacher_message.get_text())