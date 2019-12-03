# 导入unittest、三角形函数、csv读取参数类
import unittest
from Code.triangle import Triangle
from ReadData.read_csv import Read_Csv
# 实例化三角形
sjx = Triangle()
# 实例化读取csv工具
readCsvClass=Read_Csv()

# 建立测试案例
class Test_Csv(unittest.TestCase):
    def test002(self):
        # 把csv文件的数据读取调用到triangle代码中，测试三角形函数程序
        for line_list in readCsvClass.read_csv():
            result=sjx.type(int(line_list[0]),int(line_list[1]),int(line_list[2]))
            # 断言：三角新运行完后返回的结果和预期结果做对比
            self.assertEqual(result,line_list[3])
            print(line_list[0],
                  line_list[1],
                  line_list[2],
                  line_list[3], "---》test_csv验证通过")