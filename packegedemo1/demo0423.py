#能力组队

"""
输入描述
第一行代表总人数，范围1 ~ 500000
第二行数组代表每个人的能力
数组大小范围1 ~ 500000
元素取值范围1 ~ 500000
第三行数值为团队要求的最低能力值1 ~ 500000

输出描述
最多可以派出的团队数量

"""

nums = int(input())
lis = list(map(int ,input().split()))
n = int(input())
lis.sort()

res= []


for i in range(nums):
    #print(lis[i])
    if lis[i] >=n:
        res.append(lis[i])
        lis.remove(lis[i])

for i in lis:
    j = lis.index(i) + 1
    while j < len(lis):
        if lis[j] + i >=n:
            res +=[(i,lis[j])]
            lis.pop(j)
        else:
            j +=1
print(len(res))









