from bs4 import BeautifulSoup as bs
import requests
import re


urls = [
    'http://sky.nankai.edu.cn/_wp3services/generalQuery?queryObj=teacherHome'
]

form_data = {
    'siteId': '126',
    'pageIndex': '1',
    'conditions': '[{"field":"published","value":1,"judge":"="}]',
    'orders': '[{"field":"letter","type":"asc"}]',
    'returnInfos': '[{"field":"title","name":"title"},{"field":"exField1","name":"exField1"},{"field":"exField2","name":"exField2"},{"field":"exField3","name":"exField3"},{"field":"exField4","name":"exField4"},{"field":"email","name":"email"},{"field":"phone","name":"phone"},{"field":"exField5","name":"exField5"},{"field":"exField6","name":"exField6"},{"field":"exField7","name":"exField7"},{"field":"headerPic","name":"headerPic"},{"field":"cnUrl","name":"cnUrl"}]',
    'articleType': '1',
    'level': '1'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def find_teacher(url):
    response = requests.get(url, headers=headers)
    result = re.sub('\[at\]|\(at\)| at |\(~at~\)', '@', response.text, re.I)
    result = re.sub('\[dot\]|\(dot\)| dot |\(~dot~\)|．', '.', result, re.I)
    result = re.findall('([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9_\-\.]+)', result)
    return result


def find_teacher_list(url):
    with open('teacher.txt', 'a') as f:
        response = requests.post(url, headers=headers, data=form_data)
        for teacher in response.json()['data']:
            name = teacher['title']
            email_list = find_teacher(teacher['cnUrl'])
            email_list = list(set(email_list))
            print(name, email_list)
            f.write(f'生命科学学院\t{name}')
            for email in email_list:
                f.write(f'\t{email}')
            f.write('\n')

for url in urls:
    find_teacher_list(url)
