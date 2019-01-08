def solve(array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if len(array) == 1 or len(array) == 0:
        return array

    for i in range(len(array), 0, -1):
        largest_index = 0
        for j in range(i):
            if array[j] >= array[largest_index]:
                largest_index = j
        array[largest_index], array[j] = array[j], array[largest_index]
    return array


def select_sort2(list):
	for i in range(len(list)-1,0,-1): #-1避免0,1长度进入循环
		max_ind = 0
		for j in range(i+1):
			if list[j] > list[max_ind]:
				max_ind = j
list[max_ind], list[i] = list[i], list[max_ind]


x = [2,1,5,4,7,3,9]
y = solve(x)

print(y)