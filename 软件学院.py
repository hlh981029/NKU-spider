from bs4 import BeautifulSoup as bs
import requests
import re

urls = [
    'http://cs.nankai.edu.cn/index.php/zh/2017-01-15-22-19-36/2017-01-15-22-20-52',
    'http://cs.nankai.edu.cn/index.php/zh/2017-01-15-22-19-36/2017-01-15-22-20-52?start=10'
]


def find_page(url):
    response = requests.get(url)
    email_attribute = re.search('cloaked_email.*?attr\((data-ep-.*?)\).*?\((data-ep-.*?)\)', response.text)
    page = bs(response.text, 'html.parser')
    teacher_list = page.find_all("div", class_="span9")
    teacher_list = teacher_list[1:]
    with open('teacher.txt', 'a') as f:
        for teacher in teacher_list:
            name = teacher.find("a").get_text().strip()
            email_list = teacher.find_all("span")[1:]
            temp_email_1 = ""
            temp_email_2 = ""
            for email_item in email_list:
                temp_email_1 += email_item[email_attribute.group(1)]
                temp_email_2 = email_item[email_attribute.group(2)] + temp_email_2
            email = temp_email_1+temp_email_2
            print(name, email)
            f.write(f'软件学院\t{name}\t{email}\n')


for url in urls:
    find_page(url)
