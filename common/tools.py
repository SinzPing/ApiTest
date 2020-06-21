from common import function
import env
import json


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


def get_usertoken(account, pwd='E10ADC3949BA59ABBE56E057F20F883E'):
    """
    用户登录，获取token
    """
    config = choose_env(env.env)

    req = function.ApiRequest('%s/user/login' % config.url)
    text = req.post_request({'account': account, 'pwd': pwd})
    json_token = json.loads(text)
    return json_token['token']


def get_url(api):
    """
    获取请求url
    """
    config = choose_env(env.env)
    url = config.url + api

    return url


def clean_log(path):
    """
    清除文件内容
    """
    with open(path, "r+") as f:
        f.seek(0)
        f.truncate()  # 清空文件
        print('清除成功！')


if __name__ == '__main__':
    clean_log(r'D:/ApiTest/log/part_insert.log')
