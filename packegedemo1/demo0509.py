#od 猜字谜
"""
猜字谜
题目
小王设计了一个简单的猜字谜游戏，游戏的谜面是一个错误的单词，比如nesw，玩家需要猜出谜底库中正确的单词。
猜中的要求如下：
对于某个谜面和谜底单词，满足下面任一条件都表示猜中：

变换顺序以后一样的，比如通过变换w和e的顺序，nwes跟news是可以完全对应的；
字母去重以后是一样的，比如woood和wood是一样的，它们去重后都是wod
请你写一个程序帮忙在谜底库中找到正确的谜底。
谜面是多个单词，都需要找到对应的谜底，如果找不到的话，返回not found
输入：
conection
connection, today
输出：
connection
输入：
bndi,wooood
bind, wood,wrong
输出：
bind, wood
"""
# instr1 = input().strip().split(",")
# instr2 = input().strip().split(",")

def Dup2Com(str1,str2):
    #"".join((lambda x:(x.sort(),x)[1])(list(s)))
    st1 = set("".join((lambda x:(x.sort(),x)[1])(list(str1))))
    st2 = set("".join((lambda x:(x.sort(),x)[1])(list(str2))))
    return True if st1==st2 else False

def gassWords(str1,str2):
    res = []
    for i in str1:
        for j in str2:
            if i ==j:
                res.append(j)
                break
            elif  Dup2Com(i,j):
                res.append(j)
                break
    return res

# res = gassWords(instr1,instr2)
#
# if len(res):
#     print(','.join(res))
# else:
#     print("not found")
#

print((2,3)[1])
stsort= lambda x:(x.sort(),x)[1]
st = 'goddod'
print("".join(stsort(list(st))))