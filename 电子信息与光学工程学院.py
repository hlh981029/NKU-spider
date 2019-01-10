from selenium import webdriver
import re
import time

browser = None
root_url = 'http://it.nankai.edu.cn/itemis/Teachers/'
urls = [
    'Depart.aspx?did=8',
    # 'Depart.aspx?did=9',
    # 'Depart.aspx?did=32',
    # 'Depart.aspx?did=31',
    # 'Depart.aspx?did=33',
    # 'Depart.aspx?did=34',
    # 'Depart.aspx?did=12',
    # 'Depart.aspx?did=16'
]


def find_teacher(url):
    pass
    # response = requests.get(root_url+url, headers=headers)
    # result = re.sub('\[at\]|\(at\)| at |\(~at~\)', '@', response.text, re.I)
    # result = re.sub('\[dot\]|\(dot\)| dot |\(~dot~\)|．', '.', result, re.I)
    # result = re.findall('([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9_\-\.]+)', result)
    # return result


def find_teacher_list(url):
    time.sleep(1)
    browser.get(root_url+url)
    browser.delete_all_cookies()
    browser.add_cookie({'name': 'ASP.NET_SessionId', 'value': 'ax1vy1diftvm3ifg4vtfbeji'})
    browser.add_cookie({'name': 'FSSBBIl1UgzbN7N80S', 'value': 'Q_M9IDBLpEGtVhxcwYJMsZu_y_XwnNMrIBb8WfbxKuOVAhZB3yabpI7mCO9SxAPe'})
    browser.add_cookie({'name': 'FSSBBIl1UgzbN7N80T', 'value': '3I8ab1unVPFlgTHmQsqhSpB3zi98C.a4O501J6_8xGW_lTW9tslkF4CLSZq4w54EK5Xjp6wH4bC9EoDgui7p91P5jAj5pwv.t0v1GGJWS_a2K3Qb7f4BJCDoaQOIXcuZsLPbcDYWZZQLx5n1SH05OmeBQmcg7JcxNVVgtmQTZCeoKz2zd2P5bk6C9rOVmRwr_.8EhcvmjCmzK4TwgFqrOJySjHIXO_j7HOyQ62WtaGaxsmknuhXEoH8fxingl47Gk_kd4cYoELerj1Tz8dpj_YAGrKKf7W7l1yybtKMqOsNqdmOwGjXrsLsGkv_6jBJm1qL7'})
    browser.add_cookie({'name': 'UM_distinctid', 'value': '16835a887d8380-0997896c2ce10a-10306653-13c680-16835a887d9749'})
    browser.get(root_url+url)

    teacher_list = browser.find_elements_by_css_selector('#teachers > tbody > tr > td:nth-child(1) > a')
    print(teacher_list)
    # page = bs(response.text, 'html.parser')
    # teacher_list = page.select('#teachers > tbody > tr > td:nth-child(1) > a')
    # print(page.prettify())
    # with open('teacher.txt', 'a') as f:
    #     for teacher in teacher_list:
    #         time.sleep(1)
    #         print(teacher)
            # name = teacher.get_text()
            # email_list = find_teacher(teacher['href'])
            # email_list = list(set(email_list))
            # print(name, email_list)
            # f.write(f'医学院\t{name}')
            # for email in email_list:
            #     f.write(f'\t{email}')
            # f.write('\n')


for url in urls:
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    find_teacher_list(url)


