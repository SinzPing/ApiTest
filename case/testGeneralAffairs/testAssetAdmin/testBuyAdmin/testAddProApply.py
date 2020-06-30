"""
添加采购申请
author：郑平
"""

from common import function, tools
from .caseParams import addproapply
import env
import json
import unittest

config = tools.choose_env(env.env)


class AddProApply(unittest.TestCase):
    """
    新增采购申请
    """

    def setUp(self):
        print('====TestStart====')
        token = tools.get_usertoken(config.fdadmin)
        req = function.ApiRequest
        req.headers.update({'FDToken': token, 'Content-Type': 'application/json; charset=utf-8'})

    def test_case(self):
        for i in addproapply():
            api = '/educiotlogistics/purchasing-entry/add'
            rep = tools.post_request(api, json.dumps(i))
            print(rep)
            log = function.Logger(config.log_path + 'add_proapply.log')
            log.wirte(api, i, rep)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()



