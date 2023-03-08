"""
lambda表达式：
lambda表达式 fun = lambda x: x*x ---- 匿名函数名称 = lambda 参数名： 返回值
lambda [arg1 [,arg2,.....argn]]:expression
特殊用法：
lambda X:None          # 函数没有输入参数，输出是None
lambda *args: sum(args)    # 输入是任意个数参数，输出是它们的和(隐性要求输入参数必须能进行算术运算)
lambda **kwargs: 1      # 输入是任意键值对参数，输出是1

"""

#简单用法
from functools import reduce

s = lambda x:x*x
print(s(5))

s1= lambda x,y :x+y
print(s1(2,3))

"""
lambda常用高阶函数：
map()函数  遍历序列，对序列中每个元素进行函数操作，最终获取新的序列。
map(lambda,iterable)
reduce() 函数
reduce(lambda, iterable) 必须有两个参数， reduce(func,[1,2,3]) 等同于 func(func(1,2),3)
sorted() 函数
sorted(iterable, /, *, key=None, reverse=False)
filter() 函数
filter（lambda,iterable) 根据条件，排除不满足的值

"""
print([i for i in map(lambda x:x*x,[1,3,4,6])]) #[1, 9, 16, 36]
print(reduce(lambda x,y:x*y,[2,3,4]))
print(sorted([('amg',2),("fun",5),('sun',1),('dat',7)], key=lambda x:x[0]))
print([i for i in filter(lambda x:x>3,[2,5,6,1,7])])


# lis1 = [('amg',2),("fun",5),('sun',1),('dat',7)]
# print(lis1[0][1]) #2
