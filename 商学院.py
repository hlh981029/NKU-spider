from bs4 import BeautifulSoup as bs
import requests
import re

root_url = 'http://ibs.nankai.edu.cn'
urls = [
    '/teacher/bm'
]


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def find_page_list(url):
    response = requests.get(root_url+url, headers=headers)
    page = bs(response.text, 'html.parser')
    page_list = [i['href'] for i in page.select('#left-nav-ul .left_nav_1 a')]
    with open('teacher.txt', 'a') as f:
        for page_url in page_list:
            page_response = requests.get(root_url+page_url)
            teacher_page = bs(page_response.text, 'html.parser')
            teacher_list = teacher_page.select('.teacherbox')
            for teacher in teacher_list:
                name = teacher.select_one('.span9 a').get_text()
                email = re.search('([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9_\-\.]+)', teacher.select_one('.span9').get_text())
                if email is None:
                    email = ''
                else:
                    email = email.group()
                print(name, email)
                f.write(f'商学院\t{name}\t{email}\n')


for url in urls:
    find_page_list(url)
