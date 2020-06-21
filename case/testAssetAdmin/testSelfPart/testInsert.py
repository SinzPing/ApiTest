"""
自定义分类-新增
author：郑平
"""

from common import function, tools
from .caseParams import insert
import env
import unittest

config = tools.choose_env(env.env)


class PartInsert(unittest.TestCase):
    """
    新增自定义分类
    """
    api = '/educiotlogistics/customcategory'
    url = tools.get_url(api)
    req = function.ApiRequest(url)

    def setUp(self):
        print('====TestStart====')
        token = tools.get_usertoken(config.fdadmin)
        self.req.headers.update({'FDToken': token})

    def test_case(self):
        for i in insert():
            req = self.req.post_request(i)
            print(req)
            log = function.Logger(config.log_path + 'part_insert.log')
            log.wirte(self.url, i, req)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()



