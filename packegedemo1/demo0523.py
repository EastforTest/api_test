"""
有一个特异性的双端队列，该队列可以从头部到尾部添加数据，但是只能从头部移除数据。

小 A 一次执行 2n 个指令往队列中添加数据和移除数据，其中 n 个指令是添加数据(可能从头部也可以从尾部添加)

依次添加 1 到 n , n 个指令是移出数据, 现在要求移除数据的顺序为 1 到 n ，

为了满足最后输出的要求, 小 A 可以在任何时候调整队列中的数据的顺序

请问,小 A 最少需要调整几次才能满足移除数据的顺序正好是 1 到 n

## 输入

第一行一个整数 n ，表示数据范围

接下来有 2n 行,其中有 n 行为添加数据:

指令

`head add x`表示从头部添加数据

`tail add x`表示从尾部添加数据
 另外 n 行为移除数据指令,指令为 remove` 形式,表示移除一个数据

## 输出描述

一个整数，表示小 A 要调整的最小次数

示例1：
输入：

3

head add 1

remove

tail add 2

head add 3

remove

remove

输出：

1

"""

#标识是否需要调整


def remove(lis):
    print("------before remove------",  lis)
    lis = lis[1:]
    print("------after remove------", lis)
    return lis

def add(lis,index,val):
    if lis == []:
        lis.append(val)
        print("-----add to empty list----",lis)
    elif index == "tail":
        lis.append(val)
        print("-----add to tail----", lis)
    else:
        lis = [val] + lis
        print("-----add to head----", lis)
    return lis

lis = []
count = 0

while True:
    try:
        res = input()
        if "head add" in res:
            lis = add(lis,"head",res[-1])
        elif "tail add" in res:
            lis = add(lis,"tail",res[-1])
        else:
            if lis[0] == min(lis):
                lis = remove(lis)
            else:
                lis.sort()
                lis = remove(lis)
                count += 1

    except:
        break

print(count)
