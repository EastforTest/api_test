"""
给定一个N行的二维数组， 每行置顶0,1
1 1 0 0
0 0 0 1
0 0 1 1
1 1 1 1
现在需要将矩阵中的1进行翻转0，规则如下：
1） 当点击1时，该1反转为0， 并且他其他8个方位也变成0
2） 进一步的， 一个位置1变成0 ， 他的其他8个方位也变成0

给定一个数组， 经过几次点击能全部都变成0


dp[i][j] 如果是1 那么 dp[i-

"""
m_n = []

while True:
    try:
        line = input().split()
        m_n.append(line)
    except:
        break
m = len(m_n[0])
n = len(m_n)

def handOnePadding(x,y):
    if x > 0:
        if m_n[x-1][y] =="1": #上面
            m_n[x-1][y] = "0"
            handOnePadding(x-1,y)
        if y > 0 and m_n[x-1][y-1] == "1": #左上
            m_n[x - 1][y - 1] = "0"
            handOnePadding(x - 1, y-1)
        if y < m-1 and m_n[x-1][y+1] == "1":#右上
            m_n[x - 1][y + 1] = "0"
            handOnePadding(x - 1, y + 1)
    if x < n-1:
        if m_n[x+1][y] =="1": #下面
            m_n[x + 1][y] = "0"
            handOnePadding(x + 1, y )
        if y > 0 and m_n[x + 1][y-1] == "1": #左下
            m_n[x + 1][y - 1] = "0"
            handOnePadding(x + 1, y-1)
        if y < m-1 and  m_n[x + 1][y + 1] == "1": #右下
            m_n[x + 1][y +1] = "0"
            handOnePadding(x + 1,y + 1)
    if y > 0:
        if m_n[x][y-1] == "1": #左边
            m_n[x][y - 1] = "0"
            handOnePadding(x , y - 1)
    if y < m-1:
        if m_n[x][y + 1] == "1":  # 右边
            m_n[x][y + 1] = "0"
            handOnePadding(x, y + 1)
#需要点击几次
res = 0
for i in range(m):
    for j in range(n):
        if m_n[i][j] == "1":
            m_n[i][j] = "0"
            handOnePadding(i,j)
            res +=1

print(res)