#coding=utf-8
import urllib,urllib2,requests,json

def request():
	url="http://ctf5.shiyanbar.com/web/pcat/index.php"
	header={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.2; zh-CN; rv:1.9.2) Gecko/20100115 Firefox/3.6 ( .NET CLR 3.5.30729; .NET4.0E)'}
	post={"uname":"admin","pwd":"test"}
	postdata=urllib.urlencode(post)
	# req = urllib2.Request(url, post,header) #需要是json格式的参数  
	response = urllib2.urlopen(url,postdata) 
	return response.read()
	# header={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.2; zh-CN; rv:1.9.2) Gecko/20100115 Firefox/3.6 ( .NET CLR 3.5.30729; .NET4.0E)','Content-Type': 'application/x-www-form-urlencoded','Body':'uname=admin&pwd=test'}
	#添加访问身份，设置用户代理

if __name__ == '__main__':
	print request()