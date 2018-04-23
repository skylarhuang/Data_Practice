class ListNode(object):
	def __init__(self, x):
		self.val = x
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
	if head == None:
		return None
	elif head.next == None:
		return head
	else:
		prev_node = None
		next_node = None
		curr_node = head
		if curr_node != None:
			next_node = curr_node.next
			curr_node.next = prev_node
			prev_node = curr_node
			curr_node = next_node
			return curr_node


reverse(a)
