def bs(d, e):
	
	low = 0
	high = len(d) -1
	
	while low <= high:
		
		middle = (low + high)//2
		
		if d[middle] == e:
			return middle
			
		elif d[middle] > e:
			high = middle - 1
			
		else:
			low = middle + 1
			
	return -1
	

d = [1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71]
e = 5

print(bs(d,e))