count = 0

strs = "LONNNNP"

flag = False
for i in range(len(strs),0,-1):
    for j in range(0,len(strs)-i+1):
        if strs[j:j+i] == strs[j:j+i][::-1]:
            count = len(strs[j:j+i])
            print(count)
            flag = True
            break
    if flag:
        break








# # -----
#
# string = "BaabbA"
#
#
# match = []
#
# for i in string:
#    if i.isalpha():
#         match.append(i)
#
# match.sort(key=str.upper)
# string.index('aa',1,2)
#
# print(string)


#---------------------
# while True:
#     try:
#         m,n = list(map(int,input().split()))
#         x1,y1,x2,y2 = list(map(int,input().split()))
#         x = int(input())
#         y = int(input())
#         x3,y3 = list(map(int,input().split()))
#
#         dp = []
#         #比较数组是否有效
#         if m > 0 and n>0:
#             dp = [[0 for _ in range(n)] for _ in range(m)]
#             print(0)
#         else:
#             print(-1)
#         #是否能交换
#         if x1 <= len(dp)-1 and x2 <= len(dp)-1 and y1 <= len(dp[0])-1 and y2 <= len(dp[0])-1:
#             # temp = dp[x1][y1]
#             # dp[x1][y1] = dp[x2][y2]
#             # dp[x1][y1] = temp
#             print(0)
#         else:
#             print(-1)
#         #是否能插入一行
#         if x < len(dp)-1:
#             print(0)
#         else:
#             print(-1)
#         #是否能插入一列
#         if y < len(dp[0])-1:
#             print(0)
#         else:
#             print(-1)
#         #是否能查到坐标
#         if x3 <= len(dp)-1 and y3 <= len(dp[0])-1:
#             #print(x3,y3)
#             print(0)
#         else:
#             print(-1)
#     except:
#         break









# # num = int(input())
# num = 1
# res = 0
#
# count = 0
#
# for i in range(num+1):
#     res = i**2
#     if i == int(str(res)[len(str(res))-len(str(i)):len(str(res))]):
#        # print(i,res)
#         count +=1
# print(count)

#----------------按照字符出现的次数与字符ascii码排序--------------------------
#s = input()
# s = 'aaddccdc'
#
# dic = {}
#
# s = ''.join((lambda x:(x.sort(),x)[1])(list(s)))
#
# for i in s:
#     dic[i] = dic.get(i,0) + 1
#
# print(dic.items())
#
# dic = sorted(dic.items(),key = lambda x: x[1],reverse=True)
#
# print(''.join(k for k,v in dic))


#---------------取列表倒数第几个字符-------------------
# class Node(object):
#     def __init__(self,val=0) -> None:
#         self.val = val
#         self.next = None
#
# while True:
#     try:
#
#         nodes = int(input())
#         listNode = list(map(int,input().split()))
#         k = int(input())
#
#         head = Node()
#         while k:
#             head.next = Node(listNode.pop())
#             head = head.next
#             k -=1
#         print(head.val)
#     except:
#         break
#
# #-----------------------
