#数组二分查找
"""
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
奇数： [1,2,3,4,6,7,9] ---7, 3, 5
偶数： [1,2,3,4,6,7] --- 6
"""

def search2(nums,target):
    left = 0
    right = len(nums)
    while left < right:
        middle = left + (right - left) //2
        if nums[middle] > target:
            right = middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1

# nums =[1,2,3,4,6,7,9]
# print(search2(nums,6))

#删除数组元素
#示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

def removeArr(nums,val):
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow +=1
        fast += 1
    return slow

nums = [0,1,2,2,3,0,4,2]
# print(removeArr(nums,2),nums)

def remowArr1(nums,val):
    for i in nums[:]:  #需要使用列表对应的副本，不能用要删除的列表nums， 因为删除nums中的值， 会让索引移位，导致删除不调后面的值
        if i == val:
            nums.remove(i)
    return nums

print(remowArr1(nums,2))
