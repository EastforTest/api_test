class Solution:
    def permutation(self, S: str) -> List[str]:
        n=len(S)
        if n==0:
            return [""]
        res=[]
        for i in range(n):
            if S[i] in S[:i]:   #只需判断S[i]是否在S[:i]中出现过即可
                continue
            for s1 in self.permutation(S[:i]+S[i+1:]):
                res.append(S[i]+s1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.permutation("qqe"))



'''
class Solution:
    def maxDepth(self, s: str) -> int:
        #临时栈存右括号
        lis1 = []
        #记录深度的数量
        cnt = 0
        #记录到过的最大深度
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                lis1.append(')')
                cnt = 0
            elif s[i] == ')':
                lis1.pop()
                cnt += 1
            res = max(res,cnt)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))
'''
'''
class Solution:
    def StrToInt(self, s: str) -> int:
        # write code here
        s = s.strip()
        res = ""
        if s == "":
            return 0
        if s[0] == "+" or s[0] == "-" or s[0].isdecimal():

            for i in s:
                if i.isdecimal():
                    res += i
                    # print(res)
                else:
                    break
            sign = 1
            if s[0] == "+":
                sign = 1
            if s[0] == "-":
                sign = -1
            if s[0] == "+" or s[0] == "-":
                return min(max((int(res) * sign), -(2**31)), 2**31 - 1)
            if s[0].isdecimal():
                return min(max(int(s[0] + res), -(2**31)), 2**31 - 1)

'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算模板串S在文本串T中出现了多少次
# @param S string字符串 模板串
# @param T string字符串 文本串
# @return int整型
#


"""
b = "abababab"  8
a = "ababab",   6

步长 n ,
0,n
1,n+1
2,n+2
3,len(b)

循环次数 len(b) -len(a) + 1
a == b[i,i+len(a)]

num + =1
"""
'''

class Solution:
    def kmp(self, S: str, T: str) -> int:
        # write code here

        try:

            res = 0
            if len(T) >= len(S):
                for i in range(len(T) - len(S) + 1):
                    if S == T[i : (i + len(S))]:
                        print (T[i : (i + len(S))])
                        print(T[0: 5])
                        print(i,i+len(S))
                        res += 1
            return res
        except:
            pass

if __name__ == '__main__':
    sol = Solution()
    sol.kmp('ababab','abababab')

'''
'''
知识点：动态规划

动态规划算法的基本思想是：将待求解的问题分解成若干个相互联系的子问题，先求解子问题，然后从这些子问题的解得到原问题的解；对于重复出现的子问题，只在第一次遇到的时候对它进行求解，并把答案保存起来，让以后再次遇到时直接引用答案，不必重新求解。动态规划算法将问题的解决方案视为一系列决策的结果

思路：

既然与斐波那契数列相同，我们就把它放入数组中来解决。

具体做法：

step 1：创建一个长度为n+1n+1n+1的数组，因为只有n+1n+1n+1才能有下标第nnn项，我们用它记录前nnn项斐波那契数列。
step 2：根据公式，初始化第0项和第1项。
step 3：遍历数组，依照公式某一项等于前两项之和，将数组后续元素补齐，即可得到fib[n]fib[n]fib[n]。
'''
'''
class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code here
        #第0,1项直接返回1
        if number <=1:
            return 1
        temp = [0 for i in range(number +1)]
        print(temp)
        temp[0] = 1
        temp[1] = 1
        for i in range(2,number+1):
            temp[i] = temp[i-1] + temp[i-2]
        return temp[number]

if __name__ == '__main__':
    sol = Solution()
    print(sol.jumpFloor(7))
'''


"""
#进制转换

while(True):

    try:
        num = int(input(),base = 10)
        print(hex(num))
        #print(bin(input(),base = 16))
        #print(oct(input(),base = 16))
        #print(hec(input(),base = 16))
    except:
        break

"""
# 快速排序
"""
while True:
    try:
        a=int(input())
        b=set()
        for i in range(a):
            b.add(int(input()))
        for i in sorted(list(b)):
            print(i)
    except:
        break
        
"""
# 哈希表
"""
while(True):
    try:
        a = input()
        b = set()
        for i in a:
            b.add(i)
        print(len(b))
    except:
        break
"""
#坐标移动
"""
string = input()

str_list = string.split(";")
d = {}
print(str_list)
for item in str_list:
    if len(item) > 1 and item[0] in list("ADSW") and item[1:].isdecimal():
        print( d.get(item[0], 0))
        d[item[0]] = d.get(item[0],0) + int(item[1:])    #dict.get(key, default=None), 当没有value时返回的默认值
print(d)
x, y = (d["D"] - d["A"]), (d["W"] - d["S"])
print("%d,%d" % (x, y))
"""


#判断密码合格程序

"""
while True:
    try:

        line = input()
        a = 0
        b = 0
        c = 0
        d = 0
        flag = True
        for i in line:
            if i.isdigit():
                a = 1
            elif i.islower():
                b = 1
            elif i.isupper():
                c = 1
            else:
                d = 1
        for j in range(len(line) - 3):
            if line.count(line[j:j + 3]) > 1:
                flag = False
        if len(line) > 8 and (a + b + c + d) >= 3 and flag:
            print("OK")
        else:
            print("NG")
    except:
        break
"""
'''
str1 = input()

str2 = input()

str3 = ''

str4 = ''

for i in str1:
    if i == "Z":
        i = "a"
    elif i == "z":
        i = "A"
    elif i == "9":
        i = "0"
    elif i.isupper() and i != "Z":
        i = chr(ord(i) + 1).lower()
    elif i.islower() and i != "z":
        i = chr(ord(i) + 1).upper()
    elif i.isdecimal() and i != "9":
        i = str(int(i) + 1)
    str3  += i
  #  str3.append(i)
#print("".join(str3))
print(str3)
'''
'''
for i in str2:
    if i == "a":
        i = "Z"
    elif i == "A":
        i = "z"
    elif i == "0":
        i = "9"
    elif i.isupper() and i != "A":
        i = chr(ord(i) - 1).lower()
    elif i.islower() and i != "a":
        i = chr(ord(i) - 1).upper()
    elif i.isdecimal() and i != "0":
        i = str(int(i) -1 )
    str4  += i
  #  str3.append(i)
#print("".join(str3))
print(str4)
'''

