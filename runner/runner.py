'''
自动化执行器(调试中)
author: 郑平
'''

import unittest
import case.testManPower.testAssessWayConfig.testChangeCycle as case

suite = unittest.TestSuite()
cases = unittest.TestLoader().loadTestsFromTestCase(case.change_cycle())
suite.addTests(cases)

myrunner=unittest.TextTestRunner(verbosity=2)
myrunner.run(suite)
