import requests
import json


def robot_test():
    url = 'https://oapi.dingtalk.com/robot/send?access_token=a34efbd9b4f6c4e26a9a1a428bfead7338a53126fae4d10203af7ac2bbaea122'
    headers = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
    }
    message = {
        "msgtype": "text",
        "text": {
            "content": "测试"
        },
        "at": {
            "atMobiles": [

            ],
            "isAtAll": True
        }
    }

    rep = requests.post(url=url, data=json.dumps(message), headers=headers)
    print(rep.text)


if __name__ == '__main__':
    for i in range(3):
        robot_test()
