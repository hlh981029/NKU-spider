from bs4 import BeautifulSoup as bs
import requests
import re

urls = [
    'http://fcollege.nankai.edu.cn/_wp3services/generalQuery?queryObj=teacherHome'
]

form_data = [
    {
        'siteId': '34',
        'pageIndex': '1',
        'conditions': '[{"orConditions":[{"field":"exField5","value":"教授","judge":"="}]},{"field":"published","value":1,"judge":"="}]',
        'orders': '[{"field":"letter","type":"asc"}]',
        'returnInfos': '[{"field":"title","name":"title"},{"field":"exField1","name":"exField1"},{"field":"exField2","name":"exField2"},{"field":"exField3","name":"exField3"},{"field":"exField4","name":"exField4"},{"field":"email","name":"email"},{"field":"phone","name":"phone"},{"field":"exField5","name":"exField5"},{"field":"exField6","name":"exField6"},{"field":"exField7","name":"exField7"},{"field":"headerPic","name":"headerPic"},{"field":"cnUrl","name":"cnUrl"}]',
        'articleType': '1',
        'level': '1'
    }, {
        'siteId': '34',
        'pageIndex': '1',
        'conditions': '[{"orConditions":[{"field":"exField5","value":"副教授","judge":"="}]},{"field":"published","value":1,"judge":"="}]',
        'orders': '[{"field":"letter","type":"asc"}]',
        'returnInfos': '[{"field":"title","name":"title"},{"field":"exField1","name":"exField1"},{"field":"exField2","name":"exField2"},{"field":"exField3","name":"exField3"},{"field":"exField4","name":"exField4"},{"field":"email","name":"email"},{"field":"phone","name":"phone"},{"field":"exField5","name":"exField5"},{"field":"exField6","name":"exField6"},{"field":"exField7","name":"exField7"},{"field":"headerPic","name":"headerPic"},{"field":"cnUrl","name":"cnUrl"}]',
        'articleType': '1',
        'level': '1'
    }, {
        'siteId': '34',
        'pageIndex': '1',
        'conditions': '[{"orConditions":[{"field":"exField5","value":"讲师","judge":"="}]},{"field":"published","value":1,"judge":"="}]',
        'orders': '[{"field":"letter","type":"asc"}]',
        'returnInfos': '[{"field":"title","name":"title"},{"field":"exField1","name":"exField1"},{"field":"exField2","name":"exField2"},{"field":"exField3","name":"exField3"},{"field":"exField4","name":"exField4"},{"field":"email","name":"email"},{"field":"phone","name":"phone"},{"field":"exField5","name":"exField5"},{"field":"exField6","name":"exField6"},{"field":"exField7","name":"exField7"},{"field":"headerPic","name":"headerPic"},{"field":"cnUrl","name":"cnUrl"}]',
        'articleType': '1',
        'level': '1'
    }
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def find_teacher_list(url):
    with open('teacher.txt', 'a') as f:
        for data in form_data:
            response = requests.post(url, headers=headers, data=data)
            for teacher in response.json()['data']:
                name = teacher['title']
                email = teacher['exField4']
                print(name, email)
                f.write(f'外国语学院\t{name}\t{email}\n')


for url in urls:
    find_teacher_list(url)
