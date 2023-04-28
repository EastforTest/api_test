# 01 背包问题
"""
物品0--n， 包含质量和价值
背包容量m, 求背包能装的最大价值， 其中每样物品只能放入一次
步骤：
1，定义dp[i][j] 为背包能容纳的最大价值， i为取到的物品， j为背包的容量
2，推导公式：dp[i][j]
3，初始化
4，循环顺序
5，打印数组

goods[[1,15],[3,20],[4,30]]

"""

def maxBag(m, goods):
  """
  :param m:  表示背包的容量
  :param goods: 表示输入的物体
  :return:  最大的价值
  """
  #物品的数量 n
  n = len(goods)
  #定义dp[i][j] 为背包能容纳的最大价值， i为取到的物品， j为背包的容量
  dp =[[0 for _ in range(m+1)] for _ in range(n)]
  #初始化背包容量0， 放入物品时的最大价值
  for i in range(n):
      dp[i][0] = 0
  # 初始化背让如编号0的物品， 背包的价值
  for i in range(1,m+1):
      if goods[0][0] <=i:
        dp[0][i] = goods[0][1]
  for i in range(1,n):
      for j in range(1,m+1):
          #如果当前物品的重量大于当前背包的容量
          if goods[i][0] > j:
              dp[i][j] = dp[i-1][j]
          else:
              dp[i][j] = max(dp[i-1][j] ,dp[i-1][j-goods[i][0]] +goods[i][1])
  return dp[n-1][m]

goods = [[1,15],[3,20],[4,30]]

print(maxBag(4,goods))
