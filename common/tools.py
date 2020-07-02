from common import function
from time import sleep
from datetime import datetime
import env
import json
import unittest
import os


def choose_env(environment):
    """
    选择运行环境
    """
    if environment == 'dev':
        from config.dev import config
    elif environment == 'release':
        from config.release import config
    else:
        from config.test import config
    return config


def get_url(api):
    """
    获取请求url
    """
    config = choose_env(env.env)
    url = config.url + api

    return url


def post_request(api, params):
    """
    封装post接口请求
    """
    url = get_url(api)
    req = function.ApiRequest(url)
    rep = req.post_request(params)
    return rep


def get_request(api, params):
    """
    封装get接口请求
    """
    url = get_url(api)
    req = function.ApiRequest(url)
    rep = req.get_request(params)
    return rep


def get_usertoken(account, pwd='E10ADC3949BA59ABBE56E057F20F883E'):
    """
    用户登录，获取token
    """
    req = function.ApiRequest(get_url('/user/login'))
    req.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
    text = req.post_request({'account': account, 'pwd': pwd})
    json_token = json.loads(text)
    return json_token['token']


def get_suites(path, keyword):
    """
    测试套件，执行具体哪些用例
    """
    suites = unittest.TestLoader().discover(path, pattern=keyword)
    return suites


def clean_log(path):
    """
    清除文件内容
    """
    with open(path, "r+") as f:
        f.seek(0)
        f.truncate()  # 清空文件
        print('清除成功！')


def exec_time(time, cmd):
    """
    定时执行任务
    """
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print('现在的时间是： ' + now)
        sleep(1)
        if time in now:
            print('============================开始执行脚本============================')
            os.system(cmd)
            print('============================脚本执行完毕============================')
            break
    return None


if __name__ == '__main__':
    clean_log(r'D:/ApiTest/log/get_assetapplyid.log')
    # print(get_usertoken('fdadmin'))
    # print(request('/user/login', {'account': 'fdadmin', 'pwd': 'E10ADC3949BA59ABBE56E057F20F883E'}))