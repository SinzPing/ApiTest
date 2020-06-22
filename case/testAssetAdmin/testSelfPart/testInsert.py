"""
自定义分类-新增
author：郑平
"""

from common import function, tools
from .caseParams import insert
import env
import json
import unittest

config = tools.choose_env(env.env)


class PartInsert(unittest.TestCase):
    """
    新增自定义分类
    """

    def setUp(self):
        print('====TestStart====')
        token = tools.get_usertoken(config.fdadmin)
        req = function.ApiRequest
        req.headers.update({'FDToken': token, 'Content-Type': 'application/json; charset=utf-8'})

    def test_case(self):
        for i in insert():
            api = '/educiotlogistics/customcategory'
            rep = tools.request(api, json.dumps(i))
            print(rep)
            log = function.Logger(config.log_path + 'part_insert.log')
            log.wirte(api, i, rep)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()



