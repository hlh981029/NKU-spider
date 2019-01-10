from bs4 import BeautifulSoup as bs
import requests
import re
import time


root_url = 'http://env.nankai.edu.cn'
urls = [
    '/shiziduiwu/jiaoshou/',
    '/shiziduiwu/fujiaoshou/',
    '/shiziduiwu/jiangshi/'
]


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def find_teacher(url):
    response = requests.get(root_url+url, headers=headers)
    next_url = re.search('<div id="url" style="display:none;">(.*?)</div>', bytes.decode(response.content)).group(1)
    time.sleep(1)
    next_response = requests.get(root_url+next_url, headers=headers)
    result = re.sub('\[at\]|\(at\)| at |\(~at~\)', '@', bytes.decode(next_response.content), re.I)
    result = re.sub('\[dot\]|\(dot\)| dot |\(~dot~\)|．', '.', result, re.I)
    result = re.findall('([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9_\-\.]+)', result)
    return result[:-1]


def find_teacher_list(url):
    response = requests.get(root_url+url, headers=headers)
    page = bs(bytes.decode(response.content), 'html.parser')
    teacher_list = page.select('.teacherList li a')
    with open('teacher.txt', 'a') as f:
        for teacher in teacher_list:
            time.sleep(1)
            name = teacher.get_text()
            email_list = find_teacher(teacher['href'])
            email_list = list(set(email_list))
            print(name, email_list)
            f.write(f'环境科学与工程学院\t{name}')
            for email in email_list:
                f.write(f'\t{email}')
            f.write('\n')


for url in urls:
    find_teacher_list(url)

