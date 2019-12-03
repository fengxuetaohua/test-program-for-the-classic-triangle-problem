# 导包
import unittest
from Code.triangle import Triangle
from ReadData.read_txt import Read_Txt
# 实例化
sjx = Triangle()
read_txt = Read_Txt()
# 建立测试用例


class Test_Json(unittest.TestCase):
    def test003(self):
        for list in read_txt.readTxt():
            result=sjx.type(int(list[0]),int(list[1]),int(list[2]))
            # 设置断言
            self.assertEqual(list[3],result)
            # 为了查看方便，我把执行成功后的数据打印一下
            print(list[0],
                  list[1],
                  list[2],
                  list[3], "-->test_txt通过！")

