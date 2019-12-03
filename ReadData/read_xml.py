# 这个类实现了读取指定标签1下的子标签2的值
# 导包
from xml.dom import minidom


class Read_Xml:
    def __init__(self,file_name="../DataPool/triangle.xml"):
        # 加载解析 parse是minidom的一个函数
        self.dom = minidom.parse(file_name)
        # 获取对象，获取根标签body的地址
        self.root = self.dom.documentElement

    def red_xml(self,node,num,nodechild):
        # 获取根元素下面的node子标签的地址
        element=self.root.getElementsByTagName(node)[int(num)]
        # 返回第一个node子标签范围内的下一级子标签nodechild的值
        return element.getElementsByTagName(nodechild)[0].firstChild.data
    # 获取node标签的个数

    def get_len(self,node):
        return len(self.root.getElementsByTagName(node))


if __name__ == '__main__':
    print(Read_Xml().red_xml('bian',0,"b11"))
    print(Read_Xml().get_len('b1'))