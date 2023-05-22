lines = []
while True:
    try:
        res =input().split()
        lines.append(res)
    except:
        break

print(lines)
# import sys
#
# lines = sys.stdin.readlines()
#
# print(lines)
#
#
# #['YES YES YES\n', 'NO NO NO \n', 'YES NO NO\n']