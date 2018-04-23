class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


def merge(one, two):
	new = ListNode(0)

	curr_node = new
	while ((one != None) and (two != None)):
		print(one.val, two.val)
		if one.val <= two.val:
			curr_node.next = one
			one = one.next
		else:
			curr_node.next = two
			two = two.next
		curr_node = curr_node.next
	if (one != None):
		curr_node.next = one
	if (two != None):
		curr_node.next = two

	return new.next


a1 = ListNode(1)
a2 = ListNode(3)
a3 = ListNode(5)
a1.next=a2
a2.next=a3

b1 = ListNode(2)
b2 = ListNode(6)
b1.next=b2

c = merge(a1, b1)

print(c.val)

print(c.val, c.next.val, c.next.next.val, c.next.next.next.val, c.next.next.next.next.val)
