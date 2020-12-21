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
    if environment == 'dev':  # 选择开发环境
        from config.dev import config
    elif environment == 'release':  # 选择线上环境
        from config.release import config
    else:  # 选择测试环境，如果有其他环境可以自行添加
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


def get_usertoken(account, pwd='ZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2U='):
    """
    用户登录，获取token/cookie
    """
    req = function.ApiRequest(get_url('v1/web/eduaccount/sys/login'))  #
    req.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})  # 如果登录接口是表单形式的入参就用这个，如果是body入参就注释掉
    text = req.post_request({'domainName': 'zp.com', 'password': pwd, 'username': account})
    json_token = json.loads(text)
    return json_token['data']['token']  # 一般登录后会返回一个token，或者cookie，不同公司有所不同


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
        sleep(1)  # 每一秒检查一次时间有没有到，可以自行修改
        if time in now:
            print('============================开始执行脚本============================')
            os.system(cmd)
            print('============================脚本执行完毕============================')
            break
    return None


if __name__ == '__main__':
    # token = get_usertoken('13211111111')
    # print(token)
    clean_log(r'C:/Users/88000129/ApiTest/log/insert_class.log')
    # clean_log(r'C:/Users/88000129/ApiTest/log/normal.log')
