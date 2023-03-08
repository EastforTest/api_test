#矩阵
x = [[13,-1,4],[5,0,6],[1,9,-3]]
#将X拷贝到Y中
y = x.copy()
#print(y)

# y所有的值加1
'''
for row1 in range(len(x)):
    for row2 in range(len(x[row1])):
        y[row1][row2] = y[row1][row2] + 1

 # x*y
#  z [0][0] = x[0][0]*y[0][0]+x[0][1]*y[1][0]+x[0][2]*y[2][0]
'''
z =[[0 for i in range(len(x)) ] for j in range(len(y))]
for row1 in range(len(x)):
    for row2 in range(len(y)):
        for col in range(len(y[row2])):
            z[row1][row2] += x[row1][col] * y[col][row2]
print(z)

