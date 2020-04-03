import requests
import time
import json
import re
while True:
    res = requests.get('http://www.gyu.cn')
    res.encodeing = 'utf-8'

    res =res.content




    pa = re.findall('<h1><a.*>(.*)</a></h1>',res.decode('utf-8'))
    print(pa)
