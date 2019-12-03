# 导包
import json


class Read_Json:
    def read_json(self,):
        # 打开文件流
        with open("../DataPool/sjx.json","r",encoding="utf-8") as f:
            # 调用load()
            datas =json.load(f)
            return datas["data"]


if __name__ == '__main__':
    print(Read_Json().read_json())
