from bs4 import BeautifulSoup as bs
import requests
import re
import time


root_url = 'http://chem.nankai.edu.cn/'
urls = [
    'ejym_wide.aspx?m=1.2&n=-1&t=3'
]


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def find_teacher(url):
    response = requests.get(root_url+url, headers=headers)
    result = re.sub('\[at\]|\(at\)| at |\(~at~\)', '@', response.text, re.I)
    result = re.sub('\[dot\]|\(dot\)| dot |\(~dot~\)|．', '.', result, re.I)
    result = re.findall('([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9_\-\.]+)', result)
    return result


def find_teacher_list(url):
    response = requests.get(root_url+url, headers=headers)
    page = bs(response.text, 'html.parser')
    print(response.text)
    teacher_list = re.findall('arrxingming\[\d+\] = "(.*?)";\s*arryikatong\[\d+\] = "(.*?)";', response.text)
    with open('teacher.txt', 'a') as f:
        for teacher in teacher_list:
            time.sleep(1)
            print(teacher)
            name = teacher[0]
            email_list = find_teacher('dt.aspx?n='+teacher[1])
            email_list = list(set(email_list))
            print(name, email_list)
            f.write(f'化学科学学院\t{name}')
            for email in email_list:
                f.write(f'\t{email}')
            f.write('\n')


for url in urls:
    find_teacher_list(url)
