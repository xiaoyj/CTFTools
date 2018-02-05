# -*- coding:utf-8 -*-
__author__ = 'Administrator'
#from ultrapower.fd
import itertools as its
import md5

#暴力破解
def uncipher(maxlenth,salt,ciphertext_s,str_letter):
  ciphertext_s=ciphertext_s
  salt = salt
  maxlenth=int(maxlenth)
  str_letter=str_letter
  ciphertext=''
  for i in range(1, maxlenth+1):
    # 迭代生成明文(例如abc,repeat=2  结果为（a,a)(a,b)(a,c)(b,b)(b,a)(b,c)(c,c)(c,a)(c,b)
    r = its.product(str_letter, repeat=i)
    for j in r:
      plaintext = "".join(j) #连接成字符串
      plaintext = "%s%s" % (plaintext, salt)  #把盐加到明文的后面 每次生成的最终明文
      print plaintext   #打印明文
      # 开始解密，方法是，每个明文进来，加密成密文，然后密文与密文做对比
      md501 = md5.new()
      md501.update(plaintext)
      ciphertext = md501.hexdigest()
      # 对比密文确认明文
      if ciphertext == ciphertext_s:  #如果密文一致 退出2层循环
        break
    if ciphertext == ciphertext_s:    #如果密文一致，退出1层循环，打印结果
      print "task finished(plain,cipher)"
      print "%s:%s" % (plaintext, ciphertext) #打印结果
      break

#开始执行主函数
#str_letter="abcdefghijklmnopqrstuvwxyz0123456789"
#str_letter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#str_letter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_letter="abcdefghijklmnopqrstuvwxyz"   #明文的字符范围
maxlenth=6   #明文的最大长度,一般不会超过6位，否则短时间很难暴力破解
salt='5948'  #加盐 #如果不加盐，为空就是正常的md5解密
ciphertext_s='81bdf501ef206ae7d3b92070196f7e98'     #密文
uncipher(maxlenth,salt,ciphertext_s,str_letter)     #开始解密