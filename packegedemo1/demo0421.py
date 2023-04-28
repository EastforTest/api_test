#去处多余空格,打印新的关键字下标
"""
Life is painting a  picture, not doing 'a  sum'.
8 15,20 26,43 45

"""

"""
import re

inp = input()
#index = input()
pattern = r"('.*'\.)"
# quoted = re.compile("(?<=')[^']+(?=')")

lis = re.findall(pattern,inp)

temp = inp.replace(lis[0],"")

res = ' '.join(temp.split()) + " " +lis[0]

print(res)

"""

#分奖金  右边第一个比左边大的数值相减， 给出当前人呢的奖金

num = int(input())
lis = list(map(int, input().split()))

res = []

for i in range(num-1):
   # print(res)
   # print(max(lis[i + 1:]))
   if lis[i] < max(lis[i+1:]):
        for j in range(1+i,num):
                #print("lis[i] ",lis[i],"lis[j] ", lis[j])
                if lis[i] < lis[j]:
                    # print("i ",i,"j ",j)
                    res.append(str((j-i)*(int(lis[j])-int(lis[i]))))
                    break
   else:
       res.append(str(lis[i]))
res.append(str(lis[-1]))

print(' '.join(res))


#字符串消消乐
"""
字符串消消乐。相邻且相同的字符串可以消除，消除后字符继续消除，给你一串字符，给出最终的长度。字符串大小写敏感，有其他非字母字符返回0。
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

"""
"""
strs = input().strip()

lis = []

def redupStr(strs):
    for i in strs:
        if len(lis)==0:
            lis.append(i)
        elif i == lis[-1]:
            lis.pop()
        else:
            lis.append(i)
    return lis

print(''.join(redupStr(strs)))
"""