# 动态规划

"""
#入门题目， 斐波那契数列  1 1 2 3 5 8 13 21
#解题步骤
1, 定义dp[i], dp[i]代表斐波那契数列第i 个数的值
2，递推公式 dp[i] = dp[i-1] + dp[i-2]
3, dp数组的初始化,dp = [0] *n , 以及初始值： dp[0] = 1 ， dp[1] = 1,
4, 遍历顺序  从左到右
5，打印dp数组，
"""


def fanci(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
        print(dp[i])
    return dp[n-1]
#print(fanci(3))

"""
爬楼梯问题
1， 有n阶楼梯， 每次爬1步或是2步， 有多少种方法爬完
爬1 1种， 爬2， 两种 11 2 ， 爬3 111 12 21 3中， 爬4 1111 121 211 112 22 爬n阶  dp[i] = dp[i-1] + dp[i-2]
步骤1， 定义dp[i]是爬爬第i个阶梯可用的方法
2，递推公式， dp[i] = dp[i-1] + dp[i-2]
3，dp[i]*n是n个台阶， dp[0] = 0, dp[1] = 1 ,dp[2] = 2
4, 遍历顺序， 是从小道大
5，打印dp数组
"""

def stepS(n):
    dp = [0] *(n+1)
    print(dp)
    dp[1] = 1
    dp[2] = 2
    if n <= 2:
        return n
    else:
        for i in range(3,n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

#print(stepS(4))

"""
最小上楼梯花费‘
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，
可选择向上爬一个或者两个台阶。你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。请你计算并返回达到楼梯顶部的最低花费。
"""
def costLess(cos):
    dp = [0]*(len(cos)+1)
    dp[0] = 0
    dp[1] = 0
    for i in range(2,len(cos)+1):
        dp[i] = min(dp[i-1] + cos[i-1],dp[i-2] + cos[i-2])
    return dp[len(cos)]

#cos = [10,15,20]
cos = [1,100,1,1,1,100,1,1,100,1]

#print(costLess(cos))

"""
#不同路径
棋牌格子， 机器人从左到右， 从上到下有多少种路径
m*n的格子
到dp[i][j]位置是需要从位置dp[i][j-1] 位置向下， 从左位置dp[i-1][j]向下
dp[i][j] = dp[i][j-1] + dp[i][j-1]
dp[0][j] = 1 dp[i][0] = 1
"""
def sumPath(m,n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
#print(sumPath(2,2))

"""
#不同路径 II, 存在障碍的格子
棋牌格子， 机器人从左到右， 从上到下有多少种路径
m*n的格子
到dp[i][j]位置是需要从位置dp[i][j-1] 位置向下， 从左位置dp[i-1][j]向下
dp[i][j] = dp[i][j-1] + dp[i][j-1]
dp[0][j] = 1 dp[i][0] = 1
"""
def hasStock(stock):
    m = len(stock[0])
    n = len(stock)
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        if stock[i][0] == 0:
            dp[i][0] = 1
        else:
            break
    for j in range(n):
        if stock[0][j] == 0:
            dp[0][j] = 1
        else:
            break
    for i in range(1,m):
        for j in range(1,n):
            if stock[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

stock = [
  [0,0,1],
  [0,0,0],
  [0,0,0]
]

print(hasStock(stock))