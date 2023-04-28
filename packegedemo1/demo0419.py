#python 推导式

#元组推导式
a = (x for x in range(1,10))
print(type(a))
print(list(a))
#列表推导式
b = [x for x in range(1,10)]
print(b)

#计算 30 以内可以被 3 整除的整数：
c = [x for x in range(30) if x % 3 == 0]
print(c)

#过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
#names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
d = [x.upper() for x in names if len(x)>3]
print(d)
#字典推导式
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
e = {key:len(key) for key in listdemo}
print(e)
#提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
f = {x:x**2 for x in (2,3,5)}
print(f)
#集合推导式
g = {x for x in "aassdfdssdfhdfhfh" if x not in "as"}
print(g)