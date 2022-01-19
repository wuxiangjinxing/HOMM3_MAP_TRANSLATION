# coding=UTF-8

import requests
import re
import string
from fake_useragent import UserAgent
from baidu import requests_for_dst



with open('MAP3.txt','r',encoding='gbk')as f: # 文件名 例如 MAP3.txt
    text=f.read()

eList=[]
pat='Message:\n(.*?)\n\n'
pat=re.compile(pat,re.M|re.S)
result0s=pat.findall(text)
num=len(result0s)
with open('中文.txt','a+')as f1:
    for result0 in result0s:
        print(num)
        f1.write(result0)
        f1.write('\n')
        try:
            print(result0)
            if result0:
                ss=requests_for_dst(result0)
                f1.write(ss)
                str0='Messagenihao:\n'+ss+'\n'
                text=re.sub(pat,str0,text,count=1)
                num=num-1
            else:
                ss='Messagenihao:\n\n\n'
                print('空')
                f1.write(ss)
                text=re.sub(pat,ss,text,count=1)
                num=num-1
        except Exception as e:
            print(e)
            eList.append(result0)
            ss='Messagenihao:\n'+result0+'\n\n'
            print('空')
            f1.write(ss)
            text=re.sub(pat,ss,text,count=1)
            num=num-1
        f1.write('\n')
    f1.write(','.join(eList))
#print(text)

with open('new3.txt','w') as f0:  # 生成的文件名 例如 new3.txt
    f0.write(text.replace('Messagenihao:','Message:'))
    print(eList)


