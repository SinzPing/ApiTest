import requests
import time
from common import tools
from case import insert_data


class ApiRequest:
    """
    封装接口请求类型(暂时只封装get和post方法)
    """
    headers = {}

    def __init__(self, path):
        self.path = path

    def post_request(self, params):
        req = requests.post(self.path, data=params, timeout=5, headers=self.headers)
        return req.text

    def get_request(self, params):
        req = requests.get(self.path, params=params, timeout=5, headers=self.headers)
        return req.text


class Logger:
    """
    封装输出日志到本地文件中
    """

    def __init__(self, path):
        self.path = path

    def wirte(self, api, params, rep):
        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        url = tools.get_url(api)
        with open(self.path, 'a', encoding='utf-8') as f:
            f.write('请求URL： ' + url + '\n')
            f.write(localtime + '    %s' % params + '\n')
            f.write(localtime + '    ' + rep + '\n\n')
