#编写要测试的源代码
class Triangle:
    def type(self, a, b, c):
        if a+c > b and a+b > c and c+b > a:
            if a == b == c:
                return "等边三角形"
            elif a == b or b == c or b == c:
                return "等腰三角形"
            else:
                return "普通三角形"
        else:
            return "不是三角形"


if __name__ == '__main__':
    print(Triangle().type(2, 3, 2) )