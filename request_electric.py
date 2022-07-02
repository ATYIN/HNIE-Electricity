import requests
import email_mys

def get_cooki():
    cookieg = ''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    }
    response = requests.get(url="http://39.108.173.72:8080/isimshngc/loginServlet",headers=headers)
    cookieg = response.cookies
    return cookieg

if __name__ == '__main__':
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
	#data值可以查找相应的房间信息查询html文件中的value值
    data = {
        'xiaoquId':1,	#校区
        'buildingId':6,	#楼栋
        'roomName':51	#寝室号
    }
    cook = get_cooki()
    st = str(cook)[27:-31]
    headers2["Cookie"]=st
    requests.post(url = "http://39.108.173.72:8080/isimshngc/loginServlet",headers=headers2,params=data)
    response2 = requests.get(url = "http://39.108.173.72:8080/isimshngc/monServlet?monType=0", headers = headers2)
    html = str(response2.text)
    yuer = html[620:625]
    if float(yuer) <= 15:
        email_mys.send_messega('寝室电费余额不足','电费余额:'+yuer)
    else:
        print('电费余额:'+yuer)
