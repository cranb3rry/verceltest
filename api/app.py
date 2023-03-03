from flask import Flask,Response
import requests
import os
import re
from bs4 import BeautifulSoup
import time

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

strin = '''<!DOCTYPE html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport"
        content="width=350, initial-scale=1.0, maximum-scale=1.0, user-scalable=1.0, user-scalable=no;" />
    <META HTTP-EQUIV="pragma" CONTENT="no-cache">
    <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache, must-revalidate">
    <META HTTP-EQUIV="expires" CONTENT="Wed, 26 Feb 2007 08:21:57 GMT">
    <title>郑州大学数据中台2021</title>
    <link rel="stylesheet" type="text/css" href="https://jksb.v.zzu.edu.cn/imagesss/_xwss_2017.css" />
    <style>
        #bak_0 {
            MARGIN: 0 auto;
            left: 0;
            WIDTH: 350px;
            min-HEIGHT: 540px;
        }
        .hes1 {
            width: 165px;
            height: 100%;
            line-height: 20px;
            font-size: 14px;
            color: #008a24;
            text-align: center;
            background-color: #a3fdba;
            float: left;
            border-radius: 10px;
        }
        .hes2 {
            width: 165px;
            height: 100%;
            line-height: 20px;
            font-size: 14px;
            color: #909;
            text-align: center;
            background-color: #c4c4c4;
            float: left;
            border-radius: 10px;
        }
        .yim1 {
            width: 165px;
            height: 100%;
            line-height: 20px;
            font-size: 14px;
            color: #005ddc;
            text-align: center;
            background-color: #bad7ff;
            float: left;
            border-radius: 10px;
        }
        .yim2 {
            width: 165px;
            height: 100%;
            line-height: 20px;
            font-size: 14px;
            color: #909;
            text-align: center;
            background-color: #c4c4c4;
            float: left;
            border-radius: 10px;
        }
        .bar916 {
            width: 100%;
            height: 36px;
            line-height: 18px;
            font-size: 12px;
            color: #777;
            text-align: center
        }
    </style>
    <script Language="javascript">
        function zzjCallOneUrl(us) {
            document.getElementById("zzj_fun_426s").src = us;
        }
        var timeID = 0;
        var tt1 = 600;
        tt2 = 0;
        tt3 = 0;
        var timeID = setInterval("hnceTimer()", 1000);
        function hnceTimer() {
            tt1--;
            if (tt1 >= 0) {
                if ((tt1 % 2) == 1) {
                    document.getElementById('bian92a').style.backgroundColor = "REPLACECOLOR1";
                    document.getElementById('bian92b1').style.backgroundColor = "REPLACECOLOR1";
                    document.getElementById('bian92b2').style.backgroundColor = "REPLACECOLOR1";
                    document.getElementById('bian92c').style.backgroundColor = "REPLACECOLOR1";
                } else {
                    document.getElementById('bian92a').style.backgroundColor = "REPLACECOLOR2";
                    document.getElementById('bian92b1').style.backgroundColor = "REPLACECOLOR2";
                    document.getElementById('bian92b2').style.backgroundColor = "REPLACECOLOR2";
                    document.getElementById('bian92c').style.backgroundColor = "REPLACECOLOR2";
                }
                tt2 = tt1 % 60;
                tt3 = (tt1 - tt2) / 60;
                document.getElementById("tim317").innerHTML = tt3 + "分" + tt2 + "秒";
            } else { document.getElementById("tim317").innerHTML = "已作废"; }
        }
        function reloadwin916() {
            document.getElementById("msg11b").innerHTML = "正在获取郑好办防疫信息...";
            document.getElementById("zzj_fun_916s").src = "/vls6sss/zzujksb.dll/getzhbofmen?ptopid=****&sid=*****";
        }
    </script>
</head>
<body>
    <form method="POST" name="myform52" action="">
        <div id="bak_0">
            <div style="width:100%;height:88px;background:url(https://jksb.v.zzu.edu.cn/imagesss/title316_REPLACENUM.png);">
            </div>
            <div style="width:100%;height:7px;BACKGROUND-IMAGE: url(https://jksb.v.zzu.edu.cn/images/split5.png)"></div>
            <div style="width:100%; min-height:90px;">
                <div style="width:100%;height:6px;text-align:left;"></div>
                <div
                    style="width:100%;min-height:26px;line-height:26px;font-size:16px;color:#00c;font-weight:500;font-family:黑体;BACKGROUND-IMAGE:url(https://jksb.v.zzu.edu.cn/imagesss/sf_sheng4.png)">
                    <span style="color:#00a">国际学院.程思源</span>　<a
                        href="/vls6sss/zzujksb.dll/logout?ptopid=s*****B"><span
                            style="font-size:12px;;color:#00c;">〖切换账号〗</span></a><br />北校区大门东门.<span
                        style="background-color:#070;color:#ff0">入口</span><br />身份：正常出入校园本科生<span
                        style="font-size:12px;color:#333;">REPLACESTRING</span><br />
                        <span
                        style="color:#f00;font-size:12px">提醒：未检索到你今日出校记录</span>
                </div>
            </div>
            <div style="width:100%;height:15px;background-color:#090;" id="bian92a"></div>
            <div style="width:100%;height:280px;">
                <div style="width:15px;height:100%;background-color:#090;float:left" id="bian92b1"></div>
                <div style="width:320px;height:100%;float:left;text-align:center;">
                    <img src="blue.png"
                        style="height:280px;border:0px;" id="img916" />
                </div>
                <div style="width:14px;height:100%;background-color:#090;float:right" id="bian92b2"></div>
            </div>
            <div style="width:100%;height:15px;background-color:#090;" id="bian92c"></div>
            <div style="width:100%;height:7px;BACKGROUND-IMAGE: url(https://jksb.v.zzu.edu.cn/images/split5.png)"></div>
            <div style="width:100%;height:116px;">
                <div style="width:100%;height:80px;" id="msg11a">
                    <div class="hes1"><br />不再检测核酸时间</div>
                    <div style="width:20px;height:100%;float:left"></div>
                    <div class="yim1"><br />新冠疫苗接种<br />3剂次</div>
                    <div style="width:2px;height:100%;float:right"></div>
                </div>
                <div class="bar916">
                    <div style="width:50%;height:100%;float:left;font-size:12px;color:#666;line-height:20px;"
                        id="msg11b"></div>
                    <div style="width:48%;height:100%;float:right;font-size:12px;color:#666;line-height:20px;"
                        id="msg11c"><span style="color:#00a">定位河南省郑州市金水区文化路48号附近</span>　<span
                        style="color:#00a">扫码在设定区域内</span></div>
                </div>
            </div>
            <div style="width:100%;height:7px;BACKGROUND-IMAGE: url(https://jksb.v.zzu.edu.cn/images/split5.png)"></div>
            <div style="width:100%;min-height:18px;line-height:18px;font-size:12px;color:#666;text-align:center">
                郑州大学疫情防控领导小组、保卫处、信息化办公室</div>
        </div>
        <div style="width:1px;height:1px;">
            <iframe name="zzj_fun_426" id="zzj_fun_426s" src="" marginwidth="0" marginheight="0" height="100%"
                width="100%" scrolling="no" border="0" frameborder="0" allowtransparency="true"></iframe>
        </div>
        <input type="hidden" name="ptopid" value="s****B"><input type="hidden" name="sid"
            value="***">
    </form>
    <div style="width:100%;height:50px;"></div>
</body>
</html>'''

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


@app.route('/blue.png')
def get_png():
    with open("blue.png","rb") as f:
        image = f.read()
    return Response(image, mimetype="image/jpeg")
    
@app.route('/')
def hello_world():
    changes = get_change()
    if changes == None:
        return '''Not Avaliable'''
    else:
        return strin.replace("REPLACECOLOR1",changes[0][0]).replace("REPLACECOLOR2",changes[0][1]).replace("REPLACENUM",changes[1][0]).replace("REPLACESTRING",time.strftime("(%m月%d日 %H:%M获取)",time.localtime(time.time()+3600*8)))
    
@app.route('/out')
def out():
    changes = get_change()
    if changes == None:
        return '''Not Avaliable'''
    else:
        return strin.replace("REPLACECOLOR1",changes[0][0]).replace("REPLACECOLOR2",changes[0][1]).replace("REPLACENUM",changes[1][0]).replace("REPLACESTRING",time.strftime("(%m月%d日 %H:%M获取)",time.localtime(time.time()+3600*8))).replace("#070","#c0c").replace("入口","出口")
    
