# 导包
import unittest

import time
# from unittest.runner import TextTestRunner

from Tools.HTMLTestRunner import HTMLTestRunner
# 建立testsuite
discover=unittest.defaultTestLoader.discover(".","test*.py")
# 测试报告的名字
path="../Report/"
nowtime=time.strftime("%Y-%m-%d %H_%M_%S")
file_name=path+nowtime+"单元测试测试报告.html"

# TextTestRunner().run(discover)
# 生成测试报告
with open(file_name,"wb") as f:
    HTMLTestRunner(stream=f,title="单元测试测试报告", description="测试报告输出练习").run(discover)
