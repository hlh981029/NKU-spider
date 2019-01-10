from selenium import webdriver
import requests
import re


urls = [
    'http://zfxy.nankai.edu.cn/page/faculty-page'
]


def find_teacher(url):
    result = re.sub('\[at\]|\(at\)| at |\(~at~\)', '@', response.text, re.I)
    result = re.sub('\[dot\]|\(dot\)| dot |\(~dot~\)|．', '.', result, re.I)
    result = re.findall('([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9_\-\.]+)', result)
    return result


def find_teacher_list(url):
    response = requests.get(url)
    print(response.text)
    # browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    # browser.get(url)
    #
    # results = browser.find_elements_by_css_selector('#para-Content > table > tbody > tr > td > a')
    # print(results)

# with open('temp.txt', 'a') as f:
#     f.write('\n周恩来政府管理学院\n')
for url in urls:
    find_teacher_list(url)
