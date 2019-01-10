from selenium import webdriver
import re
import time

browser = None
root_url = 'http://cc.nankai.edu.cn'
urls = [
    '/teachers/search/1',
    # '/teachers/search/2',
    # '/teachers/search/3',
    # '/teachers/search/4'
]


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}


def find_teacher(url):
    response = requests.get(root_url+url, headers=headers)
    result = re.sub('\[at\]|\(at\)| at |\(~at~\)', '@', response.text, re.I)
    result = re.sub('\[dot\]|\(dot\)| dot |\(~dot~\)|．', '.', result, re.I)
    result = re.findall('([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9_\-\.]+)', result)
    return result[:-1]



def find_teacher_list(url):
    browser.get(root_url+url)
    teacher_list = browser.find_elements_by_css_selector('td')
    # response = requests.get(root_url+url, headers=headers)
    # page = bs(response.text, 'html.parser')
    # print(page.prettify())
    # teacher_list = page.select('td[data-label=姓名]')
    # with open('teacher.txt', 'a') as f:
    #     for teacher in teacher_list:
    #         print(teacher)
            # name = teacher.get_text()
            # email_list = find_teacher(teacher['href'])
            # email_list = list(set(email_list))
            # print(name, email_list)
            # f.write(f'文学院\t{name}')
            # for email in email_list:
            #     f.write(f'\t{email}')
            # f.write('\n')


for url in urls:
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    find_teacher_list(url)
