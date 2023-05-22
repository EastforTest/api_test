# strs = "Jkdi234klowe90a3"
#
# res = ""
#
# temp = []
#
# num = ""
#
# for i in strs:
#     if i.isalpha():
#         if len(num):
#             res += "*" + str(num) + "*"
#             num = ""
#         res += i
#     elif i.isnumeric():
#         temp.append(i)
#     else:
#         res += i
#     if temp:
#         num += temp.pop()
#
#
# print(res)

print([i for i in range(1,11)])

print([[0 for i in range(3)] for i in range(4)])