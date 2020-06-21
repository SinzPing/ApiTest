'''
考核方式配置-开启关闭
author: 郑平
'''

from common import tools, function
from .caseParams import way_enable
import env
import unittest

config = tools.choose_env(env.env)  # 选择环境


class WayEnable(unittest.TestCase):
    """
    查询列表
    """
    api = '/educiotmanpower/performanceappraisal/way/enable'
    url = tools.get_url(api)
    req = function.ApiRequest(url)

    def setUp(self):
        print('====TestStart====')
        token = tools.get_usertoken(config.teacher_tian)
        self.req.headers.update({'FDToken': token})

    def test_case(self):
        for i in way_enable():
            req = self.req.post_request(i)
            print(req)
            log = function.Logger(config.log_path + 'way_enable.log')
            log.wirte(self.url, i, req)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()
