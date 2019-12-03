# 导包 unittest、code里面的三角形源代码模块、ReadData里面的读取测试数据模块
import unittest
import time

from Tools.HTMLTestRunner import HTMLTestRunner

from Code.triangle import Triangle
from ReadData.read_xml import Read_Xml
# 实例化三角形，以便测试调用
sjxClass=Triangle()
# 实例化Read_Xml，以便读取测试数据
read_xmlClass=Read_Xml()
# 建立TestCase类，unittest.TestCase不用调用直接运行就会出结果。
class Test_Xml(unittest.TestCase):
    # 方法必须以test开头
    def test001(self):

        # 调用三角形程序，获取程序返回结果
        for i in range(read_xmlClass.get_len("bian")):
            result = sjxClass.type(int(read_xmlClass.red_xml("bian", i, "b1")),
                                   int(read_xmlClass.red_xml("bian", i, "b2")),
                                   int(read_xmlClass.red_xml("bian", i, "b3")))
            # 添加断言，判断三角形程序返回的结果是否符合我们预期结果
            self.assertEqual(result,read_xmlClass.red_xml("bian", i, "except"))
            print(read_xmlClass.red_xml("bian", i, "b1"),
                  read_xmlClass.red_xml("bian", i, "b2"),
                  read_xmlClass.red_xml("bian", i, "b3"),
                  read_xmlClass.red_xml("bian", i, "except"), "--》test_xml验证通过")


