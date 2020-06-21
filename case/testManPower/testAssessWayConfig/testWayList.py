'''
考核方式配置-查询列表
author: 郑平
'''

from common import tools, function
import env
import unittest

config = tools.choose_env(env.env)  # 选择环境


class WayList(unittest.TestCase):
    """
    查询列表
    """
    api = '/educiotmanpower/performanceappraisal/way/list'
    url = tools.get_url(api)
    req = function.ApiRequest(url)

    def setUp(self):
        print('====TestStart====')
        token = tools.get_usertoken(config.teacher_tian)
        self.req.headers.update({'FDToken': token})

    def test_case(self):
        req = self.req.post_request('')
        print(req)
        log = function.Logger(config.log_path + 'waylist.log')
        log.wirte(self.url, '', req)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()
