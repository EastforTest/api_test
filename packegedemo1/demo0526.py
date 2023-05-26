"""
小明每周上班都会拿到自己的工作清单，工作清单内包含n项工作，每项工作都有对应的耗时时间（单位h）和报酬,
工作的总报酬为所有已完成工作的报酬之和，那么请你帮小明安排一下工作，保证小明在指定的工作时间内工作收入最大化。

输入描述
输入的第一行为两个正整数T，n。
T代表工作时长（单位h，0<T<1000000），n代表工作数量（1<n≤3000）。
接下来是n行，每行包含两个整数t，w。
t代表该工作消耗的时长（单位h，t>0）,w代表该项工作的报酬。
输出描述
输出小明制定工作时长内工作可获得的最大报酬。

示例一
输入
40 3
20 10
20 20
20 5
输出
30

# 优先工作时长最小报酬最大的工作
# 每完成一个任务， 任务数减去1， 时间数减去任务的时间数，
"""
task = []
while True:
    try:
        task.append(list(map(int,input().split())))
    except:
        break
T = task[0][0]       #任务时间
n = task[0][1]       #工作量
tasks = task[1:]     #可选任务
#可能的报酬
res = []
#print(tasks)

# 每n个任务加起来， 如果时间小于当前时间， 则是工作的可得任务报酬

for i in range(1,n):
    for j in range(0,len(tasks)-n):
        if sum(tasks[j:n+j][0]) <= T:
            res.append(sum(tasks[j:n+j][1]))
#print(res)
print(max(res))


