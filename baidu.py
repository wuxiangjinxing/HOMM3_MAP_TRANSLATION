# coding=UTF-8

import requests
import time
import hashlib
import json
import string

#init
api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
my_appid = '20210329000750676'
cyber = 'NW7NmwFUdCVGWT9KCvPX'
lower_case = list(string.ascii_lowercase)
 
def requests_for_dst(word):# 输入字符 返回翻译后的结果
    #init salt and final_sign
    time.sleep(1)
    salt = str(time.time())[:10]
    final_sign = str(my_appid)+word+salt+cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    #区别en,zh构造请求参数
    if list(word)[0] in lower_case:
        paramas = {
            'q':word,
            'from':'en', # 英文 转中文
            'to':'zh',
            'appid':'%s'%my_appid,
            'salt':'%s'%salt,
            'sign':'%s'%final_sign
            }
        my_url = api_url+'?appid='+str(my_appid)+'&q='+word+'&from='+'en'+'&to='+'zh'+'&salt='+salt+'&sign='+final_sign
    else:
        paramas = {
            'q':word,
            'from':'en',
            'to':'zh',
            'appid':'%s'%my_appid,
            'salt':'%s'%salt,
            'sign':'%s'%final_sign
            }
        my_url = api_url+'?appid='+str(my_appid)+'&q='+word+'&from='+'zh'+'&to='+'en'+'&salt='+salt+'&sign='+final_sign
    response = requests.get(api_url,params = paramas).content
    content = str(response,encoding = "utf-8")
    json_reads = json.loads(content)
    #print(json_reads)
    results=json_reads['trans_result']
    res=''
    for result in results:
        #print(result)
        res=res+result["dst"]+'\n'
    print(res.replace('•','.'))
    return res.replace('•','.')

