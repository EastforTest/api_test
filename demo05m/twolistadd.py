from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化链表
        head = tree = ListNode()
        #判断l1,l2不为空，循环取值做加法
        val, tmp = 0, 0
        while l1 or l2:
            #设置tmp存放大于十的数据的进位
            val = tmp
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next
            tmp = val // 10
            val = val % 10

            #将结果存入链表
            tree.next = ListNode(val)
            tree = tree.next

        return head.next



