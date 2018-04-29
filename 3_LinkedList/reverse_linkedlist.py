class ListNode(object):
	def __init__(self, vava):
		self.val = vava
		self.next = None


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = None

def reverse(head):
	curr_node = head
	prev_node = None
	next_node = None

	while curr_node != None:
		next_node = curr_node.next
		curr_node.next = prev_node
		prev_node = curr_node
		curr_node = next_node

	return prev_node

def reverse2(curr_node, prev_node=None):
  next_node = curr_node.next
  curr_node.next = prev_node
  if next_node == None:
    return curr_node
  else:
    return(reverse2(next_node, curr_node))

def reverse3(head):
  curr_node = prev_node = head
  while curr_node.next:
    prev_node = curr_node
    curr_node = curr_node.next
  curr_node.next = prev_node
  prev_node.next = None
  if curr_node != head:
    prev_node = reverse3(head)
  return curr_node

def printlink(prin):
  while prin:
    print(prin.val)
    prin=prin.next

x = reverse3(a)
printlink(x)
