import get_robot_sign
import requests
import json
import time

sign = get_robot_sign.get_sign()


def robot_test():
    url = 'https://oapi.dingtalk.com/robot/send?access_token=a34efbd9b4f6c4e26a9a1a428bfead7338a53126fae4d10203af7ac2bbaea122%s' % sign
    headers = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }

    localtime = time.strftime('%H:%M', time.localtime(time.time()))
    print(localtime)
    if localtime == '19:00' or localtime == '19:01':
        message = {
            "msgtype": "text",
            "text": {
                "content": "记得写日报"
            },
            "at": {
                "atMobiles": [],
                "isAtAll": True
            }
        }
    else:
        message = {
            "msgtype": "text",
            "text": {
                "content": "吃不吃饭？"
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
