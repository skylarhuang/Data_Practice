def numberOfNodes(head):

  length = 0
    
  while head != None:
    length = length + 1
    head = head.next
      
  return length