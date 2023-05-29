"""
#https://codernav.com/3509.html
题目：微服务的集成测试
知识点深搜
时间限制：1s 空间限制：256MB 限定语言：不限
题目描述：
现在有n个容器服务，服务的启动可能有一定的依赖性（有些服务启动没有依赖），其次服务自身启动加载会消耗一些时间。
给你一个 nxn 的二维矩阵 useTime，其中 useTime[i][i]=10 表示服务 i 自身启动加载需要消耗10s，useTime[i][j]=1 表示服务 i 启动依赖服务 j 启动完成，useTime[i][k]=0，表示服务 i 启动不依赖服务 k
其实 0<= i，j，k < n。服务之间启动没有循环依赖（不会出现环），若想对任意一个服务i进行集成测试（服务i自身也需要加载），求最少需要等待多少时间。
输入描述：
第一行输入服务总量 n，之后的 n 行表示服务启动的依赖关系以及自身启动加载耗时
最后输入 k 表示计算需要等待多少时间后可以对服务 k 进行集成测试
其中 1 <= k <=n，1<=n<=100
输出描述：
最少需要等待多少时间(s)后可以对服务 k 进行集成测试
示例1
输入：
3
5 0 0
1 5 0
0 1 5
3
输出：
15
说明：
服务3启动依赖服务2，服务2启动依赖服务1，由于服务1,2,3自身加载需要消耗5s，所以5+5+5=15，需等待15s后可以对服务3进行集成测试

"""
#多少组线程
n = int(input())
#每组线程
lis = []
for i in range(n):
    lis.append(list(map(int,input().split())))
#需要启动哪一组任务
k = int(input())

def startK(k):
    times = []  #所依赖的服务的启动时间集合
    for i in range(n):
        if k != i and lis[k][i] == 1:  #需要剔除服务本身
            times.append(startK(i))

    res = 0   #所依赖的服务的最长启动时间
    for time in times:
        res = max(res,time)
    return res + lis[k][k]  #需要加上本身的启动时间

print(startK(k-1))

# needSub = []
# needadd = []

# def isrelied(m):
#     flag = True
#     for i in range(n):
#         if m > 1 and i != m-1 and lis[m-1][i] == 0 and flag:
#             flag = True
#         elif m == 1 and i !=0 and lis[0][i] == 0 and flag:
#             flag = True
#         elif i == m-1:
#             flag = True
#         else:
#             flag = False
#
#     return flag
#
#
# def waitTime(m):
#
#     needadd.append(lis[m - 1][m - 1])
#     for i in range(n):
#         if lis[m-1][i] == 1 and m-1 != i:
#             waitTime(i+1)
#             print("needadd 内循环 ", m - 1, needadd)
#     if isrelied(m):
#         needSub.append(lis[m-1][m-1])
#         print("needSub  ", needSub)
#     return needadd
#
# if len(needSub) > 1:
#     print(sum(waitTime(k)) + max(needSub))
# else:
#     print(sum(waitTime(k)))


