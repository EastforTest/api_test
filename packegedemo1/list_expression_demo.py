"""
基本语法：
[expression for iter_val in iterable]

[expression for iter_val in iterable if cond_expr]

"""


#列表解析式

# lis1 = []
# for i in range(1,10):
#     lis1.append(i)
# print(lis1)

print([i for i in range(1,10)])

print([i*2 for i in range(1,10)])

#带筛选条件的解析式
print([i for i in range(1,10) if i > 5])

#嵌套循环

print([(m,n) for m in range(5) for n in range(5)])

#字典解释式
dis = {"hell":2,"jjse":4,"asd":8}

print({key:value for key, value in dis.items() if key == 'asd'})
