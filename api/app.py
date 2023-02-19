from flask import Flask
import requests
import os
import re
from bs4 import BeautifulSoup

app = Flask(__name__)

uid = os.environ.get('UID')
upw = os.environ.get('UPW')

headers = {
    "Origin": "https://jksb.v.zzu.edu.cn",       
    "Referer": "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0?fun2=s&door=",
    "User-Agent": "Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13",
    "Host": "jksb.v.zzu.edu.cn"
}

header2 = {
    "Referer": "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login",
    "User-Agent": "Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13",
    "Host": "jksb.v.zzu.edu.cn"
}

data ={   
    "uid": uid, 
    "upw": upw, 
    "smbtn": "领取郑州大学通行码", 
    "hh28": "664",
    "fun2": "s",
    "door": ""
}

def get_change():
    a = requests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login",headers=headers,data=data)
    soup = BeautifulSoup(a.text, 'html.parser')
    datas = soup.find('script')
    datas = datas.string
    pattern = re.compile(r'window.location="(http.*?)"', re.I | re.M)
    url = pattern.findall(datas)
    if len(url) == 0:
        return None
    else:
        b = requests.get(url[0],headers=header2)
        color = list(set(re.findall('style.backgroundColor="(.*?)"',b.text)))
        num = re.findall('title316_(.*?).png',b.text)
        if len(color)<2 or len(num) < 1:
            return None
        return color,num

@app.route('/')
def hello_world():
    return 'Index'

