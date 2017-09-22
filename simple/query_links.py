"""
快速找到单链表中间节点：
使用两个指针的方法，这个方法是面试题的正解。一个指针(P1)每次步进一个节点，另一个指针(P2)每次步进两个节点。当P2遍历到链表尾时，P1正好遍历到中间节点
"""

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


n9 = Node("n1", None)
n6 = Node("n1", n9)
n8 = Node("n1", n6)
n7 = Node("n1", n8)
n1 = Node("n1", n7)
n2 = Node("n2", n1)
n3 = Node("n3", n2)
n4 = Node("n4", n3)
n5 = Node("n5", n4)

head = n5  # 链表的头节点

P1 = head  # 一次步进1个node
P2 = head  # 一次步进2个node

while P2.next is not None and P2.next.next is not None:
    P2 = P2.next.next
    P1 = P1.next

print(P1.data)