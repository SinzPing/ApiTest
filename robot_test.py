from bs4 import BeautifulSoup
import get_robot_sign
import requests
import json
import urllib.request
import xpinyin
import time
sign = get_robot_sign.get_sign()


def get_weather(city):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    website = "http://www.tianqi.com/" + city + ".html"
    req = urllib.request.Request(url=website, headers=header)
    page = urllib.request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode("utf-8"), "html.parser")  # html.parser表示解析使用的解析器
    nodes = soup.find_all('dd')
    weather = ""
    for node in nodes:
        temp = node.get_text()
        if temp.find('[切换城市]'):
            temp = temp[:temp.find('[切换城市]')]
        weather += temp
    return weather


def robot_test():
    url = 'https://oapi.dingtalk.com/robot/send?access_token=a34efbd9b4f6c4e26a9a1a428bfead7338a53126fae4d10203af7ac2bbaea122%s' % sign
    headers = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
    }

    localtime = time.strftime('%H:%M', time.localtime(time.time()))
    print(localtime)
    if localtime == '11:35' or localtime == '17:55':
        message = {
            "msgtype": "text",
            "text": {
                "content": "准备干饭了，干饭了。"
            },
            "at": {
                "atMobiles": [],
                "isAtAll": True
            }
        }
    else:
        pin = xpinyin.Pinyin()
        city = pin.get_pinyin("深圳", "")
        today_weather = get_weather(city)
        message = {
            "msgtype": "text",
            "text": {
                "content": today_weather
            },
            "at": {
                "atMobiles": [],
                "isAtAll": True
            }
        }
    rep = requests.post(url=url, data=json.dumps(message), headers=headers)
    print(rep.text)


if __name__ == '__main__':
    robot_test()


