"""
自定义分类-删除
author：郑平
"""

from common import function, tools
from .caseParams import delete
import env
import unittest

config = tools.choose_env(env.env)


class PartDelete(unittest.TestCase):
    """
    删除自定义分类
    """
    api = '/educiotlogistics/customcategory/{id}/delete'
    url = tools.get_url(api)
    req = function.ApiRequest(url)

    def setUp(self):
        print('====TestStart====')
        token = tools.get_usertoken(config.fdadmin)
        self.req.headers.update({'FDToken': token})

    def test_case(self):
        for i in delete():
            req = self.req.post_request(i)
            print(req)
            log = function.Logger(config.log_path + 'part_delete.log')
            log.wirte(self.url, i, req)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()


