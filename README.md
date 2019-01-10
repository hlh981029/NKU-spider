# NKU-spider
南开大学教师邮箱爬虫
## 简介
使用BS4、requests和Selenium库分学院爬取了南开大学各学院老师的邮箱。

## 使用
```shell
pip install BeautifulSoup4 requests Selenium
python xx.py
```
`teacher.txt`文件格式：
> 学院`\t`姓名`\t`邮箱1`\t`……`\t`邮箱n`\n`

## 需要解决的问题：
- [ ] 无错误处理，超时会报异常
- [ ] 计算机、网安、周政、电光爬不下来，Selenium也不行
- [ ] 邮箱识别不够完善，目前只处理了`(at)`，`[at]`，` at `，`(~at~)`和对应的`dot`
