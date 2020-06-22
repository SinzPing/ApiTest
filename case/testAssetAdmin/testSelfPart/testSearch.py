"""
自定义分类-查询
author：郑平
"""

from common import function, tools
from .caseParams import search
import env
import json
import unittest

config = tools.choose_env(env.env)


class PartSearch(unittest.TestCase):
    """
    查询自定义分类
    """
    api = '/educiotlogistics/customcategory/queryForPage'
    url = tools.get_url(api)
    req = function.ApiRequest(url)

    def setUp(self):
        print('====TestStart====')
        token = tools.get_usertoken(config.fdadmin)
        self.req.headers.update({'FDToken': token, 'Content-Type': 'application/json; charset=utf-8'})

    def test_case(self):
        for i in search():
            req = self.req.post_request(json.dumps(i))
            print(req)
            log = function.Logger(config.log_path + 'part_search.log')
            log.wirte(self.url, i, req)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()


