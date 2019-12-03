class Read_Txt():
    def readTxt(self):
        # 打开txt文件流
        with open("../DataPool/sjx.txt","r",encoding="utf-8") as f:
            # 通过文件流调用读取的方法读取数据--->所有行
            datas=f.readlines()
            # 新建列表 --》添加分割后的单行列表数据，lines存放读取的数据
            lines=[]
            # 遍历
            for data in datas:
                '''
                strip():去除字符串前后回车
                split():使用指定符号进行分割字符串并以列表格式返回分割后的数据
                '''
                # 把分割后的单行列表数据添加到整体的列中，并返回
                lines.append(data.strip().split(","))
            # 如果txt文档第一行是标题，则可以从第二行开始返回，list每个元素为文件的一行数据，每个元素里又有n个元素，为文件一行的n个数据

            return lines[1:]




    '''
    f.read() #读取所有数据，不适合有大量数据的txt文档
    f.readline() # 读取单行
    f.readlines() # 读取所有行，不适合有大量数据的txt文档
    '''

if __name__ == '__main__':
    print(Read_Txt().readTxt())




