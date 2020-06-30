"""
获取采购申请单号
author：郑平
"""

from common import function, tools
import env
import unittest

config = tools.choose_env(env.env)


class GetAssetApplyId(unittest.TestCase):
    """
    获取采购申请单号
    """

    def setUp(self):
        print('====TestStart====')
        token = tools.get_usertoken(config.fdadmin)
        req = function.ApiRequest
        req.headers.update({'FDToken': token, 'Content-Type': 'application/json; charset=utf-8'})

    def test_case(self):
        api = '/educiotlogistics/purchasing-entry/getId'
        rep = tools.get_request(api, '')
        print(rep)
        log = function.Logger(config.log_path + 'get_assetapplyid.log')
        log.wirte(api, '', rep)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()



