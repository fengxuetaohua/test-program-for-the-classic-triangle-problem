# 导包
import csv


class Read_Csv():
    def read_csv(self, filename="../DataPool/sjx.csv"):
        # data_list=[]
        with open(filename, "r", encoding="utf-8") as f:
            datas = csv.reader(f)
            # for data in datas:
            #     data_list.append(data)
            return list(datas)


if __name__ == '__main__':
    print(Read_Csv().read_csv())