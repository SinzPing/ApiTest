'''
考核权重配置-查询列表
author: 郑平
'''

from common import tools, function
import env
import unittest

config = tools.choose_env(env.env)  # 选择环境


class WeightList(unittest.TestCase):
    """
    查询列表
    """
    api = '/educiotmanpower/performanceappraisal/weight/list'
    url = tools.get_url(api)
    req = function.ApiRequest(url)

    def setUp(self):
        print('====TestStart====')
        token = tools.get_usertoken(config.teacher_tian)
        self.req.headers.update({'FDToken': token})

    def test_case(self):
        rep = self.req.post_request('')
        print(rep)
        log = function.Logger(config.log_path + 'weight_list.log')
        log.wirte(self.url, '', rep)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()
