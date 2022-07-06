import requests
import email_mys
import re

def get_cooki():
    cookieg = ''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    }
    response = requests.get(url="http://39.108.173.72:8080/isimshngc/loginServlet",headers=headers)
    cookieg = response.cookies

    # print( response.status_code) #状态码
    # # print(response.text)
    # print(cookieg)
    return cookieg

if __name__ == '__main__':
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    data = {
        'xiaoquId':1,
        'buildingId':6,
        'roomName':517
    }
    cook = get_cooki()
    # print(cook)
    # print(type(cook))
    st = str(cook)[27:-31]
    # print(st)
    headers2["Cookie"]=st
    # print(headers2)
    requests.post(url = "http://39.108.173.72:8080/isimshngc/loginServlet",headers=headers2,params=data)
    response2 = requests.get(url = "http://39.108.173.72:8080/isimshngc/monServlet?monType=0", headers = headers2)
    # print(response2.text)
    html = str(response2.text)
    # print(html)
    # a = html.find('<div class="head1">剩余充值电量(度)</div>')
    # print(a)
    styuer = str(html[620:630])
    number = re.findall("\d+",styuer)
    yuer = number[0]+'.'+number[1] 
    # print(number)
    # print(yuer)
    # print(type(yuer))
    if float(yuer) <= 10:
        email_mys.send_messega('寝室电费余额不足','电费余额:'+yuer)
    else:
        print('电费余额:'+yuer)

