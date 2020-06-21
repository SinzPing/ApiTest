'''
多角色计分比重配置-查询列表
author: 郑平
'''

from common import tools, function
from .caseParams import set_rolepercent
import env
import unittest

config = tools.choose_env(env.env)  # 选择环境


class SetPercent(unittest.TestCase):
    """
    设置权重
    """
    api = '/educiotmanpower/performanceappraisal/multirole/setPercent'
    url = tools.get_url(api)
    req = function.ApiRequest(url)

    def setUp(self):
        print('====TestStart====')
        token = tools.get_usertoken(config.teacher_tian)
        self.req.headers.update({'FDToken': token})

    def test_case(self):
        for i in set_rolepercent():
            rep = self.req.post_request(i)
            print(rep)
            log = function.Logger(config.log_path + 'set_rolepercent.log')
            log.wirte(self.url, i, rep)

    def tearDown(self):
        print('====TestEnd====')


if __name__ == '__main__':
    unittest.main()
