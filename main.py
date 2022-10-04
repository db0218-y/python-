from sympy import *

while True:
    print("请选择功能 1求导  2积分")
    Choose = int(input())
    x = Symbol('x')
    if Choose == 1:
        print('请输入函数关系式：')
        y = input()  # 输入函数关系式
        # 求一阶导函数
        df1 = diff(y, x)
        # 求二阶导函数
        df2 = diff(y, x, 2)
        print('一阶导数为：')
        print(df1)
        print('二阶导数为：')
        print(df2)
    elif Choose == 2:
        print('请输入函数关系式：')
        y = input()  # 输入函数关系式
        count = integrate(y, x)
        print("该函数的积分为：", '(', count, ')', '+C')
    else:
        print("输入有误程序重新执行")
