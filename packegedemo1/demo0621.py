'''
请使用函数递归，打印如下菱形图案。（其中第四行左右两端各有一个空格，其他部分对齐即可）
    #
   ###
  #####
 #######
  #####
   ###
    #

'''
# center(9," ") 每行多少数量，其余字符代替

n = 7

def diamond(s):
    a = "#" * (2 * (n - s) + 1)
    print(a.center( n + 2, " ")) #上半部分
    if len(a) == n:
        return
    if s != 1:
        diamond(s - 1)
        print(a.center(n + 2, " ")) #下半部分


diamond(7)