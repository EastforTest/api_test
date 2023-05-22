#链节点类
class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
#链表类
class SingleLinkedList:
    #判断链表是否为空，__head指向None,则为空
    def is_empty(self):
        return self._head==None

    #单向列表初始化
    def __init__(self,node=None):
        #判断node是否为空
        if node !=None:
            headNode = Node(node)
            self._head = headNode
        else:
            self._head = node
    #计算列表长度
    def length(self):
        count = 0
        curNode = self._head
        while curNode !=None:
            count +=1
            curNode = curNode.next
        return count
    #遍历链表
    def travel(self):
        curNode=self._head
        while curNode !=None:
            print(curNode.val,end="\t")
            curNode =curNode.next
        print(" ")
    #在头部添加元素
    def add(self,val):
        #将传入的值构造成节点
        node = Node(val)
        #将新节点的连接域next指向头节点
        node.next = self._head
        #将链表的头_head指向新节点
        self._head = node

    #在尾部添加元素
    def append(self,val):
        #将传入的值构造成节点
        node = Node(val)
        if self.is_empty():#单链表为空
            self._head=node
        else: #单链表不为空
            curNode = self._head
            while curNode.next!=None:
                curNode = curNode.next
            curNode.next = node

    #在指定位置添加元素
    def insert(self,pos,val):
        #如果pos<=0,默认插入到头部
        if pos<=0:
            self.add(val)
        #如果pos>链表长度， 直接添加在尾部
        elif pos>(self.length()-1):
            self.append(val)
        else:
            #构造节点
            node =Node(val)
            count = 0
            curNode = self._head
            while count <(pos - 1):
                count += 1
                curNode = curNode.next
            #修改指向
            #将前一个节点的next指向插入的节点的下一个节点
            node.next = curNode.next
            #将插入位置的前一个节点next指向新节点
            curNode.next = node
    #查找节点是否存在
    def search(self,val):
        curNode = self._head
        while curNode !=None:
            if curNode.val == val:
                return True
            curNode = curNode.next
        return False
    #删除节点
    def remove(self,item):
        dummy_node = Node(next=self._head)
        curNode = dummy_node
        while curNode !=None:
            if curNode.val == item:
                curNode.next = curNode.next.next
                break
            else:
                curNode = curNode.next
    def deleteIndex(self,index):
        if index <0 or index >=self.length():
            return "位置错误"
        pre = self._head
        while(index):
            pre = pre.next
            index -= 1
        pre.next = pre.next.next

if __name__ == '__main__':
    singleLinkedList = SingleLinkedList(30)
    print("是否为空列表：",singleLinkedList.is_empty())
    print("链表长度为： ",singleLinkedList.length())
    print("----遍历链表----")
    singleLinkedList.travel()
    print("-----查找-----", singleLinkedList.search(30))
    print("-----头部插入-----")
    singleLinkedList.add(1)
    singleLinkedList.add(2)
    singleLinkedList.add(3)
    singleLinkedList.travel()
    print("-----尾部追加-----")
    singleLinkedList.append(10)
    singleLinkedList.append(20)
    singleLinkedList.travel()
    print("-----链表长度-----", singleLinkedList.length())
    print("-----指定位置插入-----")
    singleLinkedList.insert(-1, 100)
    singleLinkedList.insert(3, 88)
    singleLinkedList.travel()
    print("-----根据val删除节点-----")
    singleLinkedList.remove(30)
    singleLinkedList.travel()
    print("-----根据index删除节点-----")
    singleLinkedList.deleteIndex(2)
    singleLinkedList.travel()