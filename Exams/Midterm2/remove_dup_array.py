x = None

def RemoveDup(string):
  if string == None:
    return None
  else:
	  list_str = list(string) #First we convert the string to a list
	  res = []
	  ind = 0
	  while ind<len(string):
	    if len(res)==0:
	      res.append(list_str[ind])
	    elif list_str[ind] in res:
	      ind = ind+1
	    else:
	      res.append(list_str[ind])
	  return ''.join(res)
	  
print(RemoveDup(x))
