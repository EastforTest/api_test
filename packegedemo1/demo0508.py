"""
题目描述
有N条线段，长度分别为a[1]-a[n]。

现要求你计算这N条线段最多可以组合成几个直角三角形。

每条线段只能使用一次，每个三角形包含三条线段。

输入描述
第一行输入一个正整数T（1<＝T<＝100），表示有T组测试数据.

对于每组测试数据，接下来有T行，

每行第一个正整数N，表示线段个数（3<＝N<＝20），接着是N个正整数，表示每条线段长度，（0<a[i]<100）。

输出描述
对于每组测试数据输出一行，每行包括一个整数，表示最多能组合的直角三角形个数

用例
输入	1
7 3 4 5 6 5 12 13
输出	2
说明	可以组成2个直角三角形࿰
"""
#
# T = int(input()) #表示几组测试数据
#
# test = input().split() #表示输入的测试数据
#
# N = int(test[0]) # 表示输入的测试数据的第一个数，这行有几个测试数据
# data = test[1:].sort() #按照正序排序
#
#
#
# def samk():
#     count = 0  # 表示有几个是直角三角形
#     a1 = data[0:-2]
#     a2 = data[1:-1]
#     a3 = data[2:]
#     for i in range(N-2):
#         for j in range(N-2):
#             while a1 and a2 and a3:
#                 if a1[i]**2 + a2[j]**2 == a3[j]**2:
#                     count +=1
#                     a1.pop(i)
#                     a2.pop(j)
#                     a3.pop(j)
#     return count

#输入: ["10", "6", "9", "3", "+", "-11", " * ", "/", " * ", "17", "+", "5", "+"]
# 输出: 22

#from operator import add ,sub,mul

def mathed(arr):
    #op = {"+":add,"-":sub,"*":mul,"/":lambda x,y:int(x/y)}
    res = []
    if len(arr) <=2:
        return -1
    else:
        for i in arr:
            if i not in {"+","-","*","/"}:
                res.append(int(i))
            else:
                op1 = res.pop()
                op2 = res.pop()
                res.append(int(eval(f'{op2} {i} {op1}')))
        return res.pop()

arr = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(mathed(arr))


