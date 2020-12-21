"""
接口示例
author：郑平
"""

from common import function, tools
from .caseParams import abnormal, normal
import env
import json
import unittest

config = tools.choose_env(env.env)  # 选择对应环境的配置文件


class Demo(unittest.TestCase):
    """
    接口demo
    """

    def setUp(self):
        """
        用户登录（一般在接口请求之前都会校验用户是否登录）
        """
        print('====TestStart====')
        token = tools.get_usertoken(config.name)  # 选择对应登录的账号以获取token/cookie
        req = function.ApiRequest
        # req.headers.update({'x-access-token': token})  # post普通的表单入参（填充header，表示自己登录了）
        req.headers.update({'x-access-token': token, 'Content-Type': 'application/json; charset=utf-8'})  # post的body入参（填充header，表示自己登录了）

    def test_case(self):
        """
        晨午检异常上报
        """
        for i in abnormal():  # 编辑caseParams.demo方法中的接口参数
            api = 'v1/web/edugarden/amInspection/abnormalReport'
            # rep = tools.get_request(api, i)  # 这是get方式的接口请求
            rep = tools.post_request(api, json.dumps(i))  # 这是post方式的接口请求
            print(rep)
            log = function.Logger(config.log_path + 'abnormal.log')  # 需要写入log的文件名
            log.wirte(api, i, rep)
    #
    # def test_case(self):
    #     """
    #     晨午检批量正常
    #     """
    #     for i in normal():  # 编辑caseParams.demo方法中的接口参数
    #         api = 'v1/web/edugarden/amInspection/batchSave'
    #         # rep = tools.get_request(api, i)  # 这是get方式的接口请求
    #         rep = tools.post_request(api, i)  # 这是post方式的接口请求
    #         print(rep)
    #         log = function.Logger(config.log_path + 'normal.log')  # 需要写入log的文件名
    #         log.wirte(api, i, rep)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()



