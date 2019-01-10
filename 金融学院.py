from bs4 import BeautifulSoup as bs
import requests
import re

root_url = 'http://finance.nankai.edu.cn'
urls = [
    '/f/teacher/teacher/qzjs'
]


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def find_page(url):
    response = requests.get(root_url+url)
    page = bs(response.text, 'html.parser')
    # print(page.prettify())
    teacher_list = page.select('.teachImgList')
    with open('teacher.txt', 'a') as f:
        for teacher in teacher_list:
            name = teacher.select_one('.lead').get_text()
            email = teacher.select_one('.mailBox').get_text()
            print(name, email)
            f.write(f'金融学院\t{name}\t{email}\n')


for url in urls:
    find_page(url)
