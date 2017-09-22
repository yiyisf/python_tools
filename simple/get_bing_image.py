"""
自动抓取Bing首页背景高清图片并保存
"""
import requests
import json

url = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&nc=0&pid=hp&video=1"
base_url = "http://cn.bing.com"

r = requests.get(url=url)

j = json.loads(r.text)

def save_image(url):
    image = requests.get(base_url + url)
    name = 'image/' + url.split('/')[-1]
    print(name)
    with open(name, mode='wb') as f:
        f.write(image.content)

for image in j['images']:
    save_image(image['url'])


