from common import tools
import unittest


class Runner:
    """
    用例执行器
    """

    suites = tools.get_suites('case.testGeneralAffairs.testAssetAdmin', 'test*.py')
    # suite2 = tools.get_suites('path', 'keyword')
    # allsuite = unittest.TestSuite((suites, suite2))  # 如果有很多路径下有测试用例，就用此方法

    def text_runner(self):
        runner = unittest.TextTestRunner()
        result = runner.run(self.suites)
        # result = runner.run(self.allsuite)
        print(result)


if __name__ == '__main__':
    Runner().text_runner()




