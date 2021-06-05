from common import tools
import unittest


class Runner:
    """
    用例执行器
    """

    suites = tools.get_suites('case', 'test*.py')  # 路径（case.path，多个文件夹）和文件，以test开头的所有文件

    # suite2 = tools.get_suites('path', 'keyword')
    # allsuite = unittest.TestSuite((suites, suite2))  # 如果有很多路径下有测试用例，就用此方法

    def text_runner(self):
        runner = unittest.TextTestRunner()
        result = runner.run(self.suites)
        # result = runner.run(self.allsuite)
        print(result)


if __name__ == '__main__':
    Runner().text_runner()
