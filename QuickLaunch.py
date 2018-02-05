#coding:utf-8

import requests
import base64

url="http://ctf5.shiyanbar.com/web/10/10.php"
res=requests.get(url).headers['FLAG']
v=base64.b64decode(res)
print requests.post(url=url,data={'key':v.split(':')[1]}).text
a:2:{s:4:"user";b:1;s:4:"pass";b:1;}