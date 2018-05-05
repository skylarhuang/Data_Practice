class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
  def insert(self, head, value):
    
    insert_ListNode = ListNode(value)
    
    if head==None:
      insert_ListNode.next = None
      return insert_ListNode
      
    elif value<=head.val:
      insert_ListNode.next = head
      return insert_ListNode
      
    else:
      curr = head
      while curr.next and (curr.next.val<value):
        curr = curr.next
      insert_ListNode.next = curr.next
      curr.next = insert_ListNode
      return head
        
a1 = ListNode(1)
a2 = ListNode(3)
a3 = ListNode(5)
a1.next=a2
a2.next=a3
a3.next=None

a = None

def print_link(p):
    while p:
        print(p.val)
        p = p.next
        

b = Solution()
c = b.insert(a1,33)
print_link(c)
