# 导包
import unittest
from Code.triangle import Triangle
from ReadData.reader_json import Read_Json
# 实例化
sjx = Triangle()
read_json = Read_Json()
# 建立测试用例


class Test_Json(unittest.TestCase):
    def test003(self):
        for dict in read_json.read_json():
            result=sjx.type(int(dict.get("b1")),int(dict.get("b2")),int(dict.get("b3")))
            # 设置断言
            self.assertEqual(dict.get("except"),result)
            # 为了查看方便，我把执行成功后的数据打印一下
            print(dict.get("b1"),
                  dict.get("b2"),
                  dict.get("b3"),
                  dict.get("except"), "-->test_json验证通过！")

